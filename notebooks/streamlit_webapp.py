#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import os


# In[6]:


st.title('Rate my run')
st.header('Upload your planned activity of see the difficulty rating')


# In[7]:


def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)

filename = file_selector()
st.write('You selected `%s`' % filename)


# In[10]:


# read proposed route
import gpxpy

gpx_file = open(filename, 'r')
gpx = gpxpy.parse(gpx_file)

try: 
    data = gpx.tracks[0].segments[0].points
except:
    print('gpx does not have tracks')
    
try:
    data = gpx.routes[0].points
except:
    print('gpx does not have routes')

start = data[0]
finish = data[-1]
print(start)
print(finish)
df = pd.DataFrame(columns=['lon', 'lat', 'alt'])

for point in data:
    df = df.append({'lon': point.longitude, 'lat' : point.latitude, 'alt' : point.elevation}, ignore_index=True)
    


# In[44]:


# get parameters from gpx
import geopy.distance

distance = [];
elevation = [];
for i in range(len(df)-1):
    coords_1 = [df['lat'][i], df['lon'][i]]
    coords_2 = [df['lat'][i+1], df['lon'][i+1]]
    #print(coords_1, coords_2)
    distance.append(geopy.distance.vincenty(coords_1, coords_2).miles)
    elevation.append( df['alt'][i+1]-df['alt'][i])
#print(distance)
total_distance = np.sum(distance)

elevation = np.array(elevation)
gain = np.sum(elevation[np.where( elevation > 0 )])
loss = np.sum(elevation[np.where( elevation < 0 )])
gain_ft = gain*3.28084
loss_ft = loss*3.28084

longitude = df['lon'].mean()
latitude = df['lat'].mean()
high = df['alt'].max()
low = df['alt'].min() 


# In[48]:


X_test = {'length' : total_distance, 'ascent' : gain_ft, 'descent' : loss_ft, 
                        'high' : high, 'low' : low, 'longitude' : longitude, 'latitude' : latitude}


# In[56]:


#X_test = [total_distance, gain_ft, loss_ft, high, low, longitude, latitude]
X = pd.DataFrame.from_dict(X_test, orient = 'index')


# In[49]:


#Load the trained ML model
import pickle
pkl_filename = "pickle_model.pkl"
with open(pkl_filename, 'rb') as file:   
    MLmodel = pickle.load(file)


# In[62]:


#Ingest user input into trained ML model
y_predicted = MLmodel.predict(X.T)


# In[63]:

st.write('The difficulty of the route is {y}'.format(y = y_predicted))



# In[ ]:

st.map(df)


