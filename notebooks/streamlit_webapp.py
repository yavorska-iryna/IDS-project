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


# In[ ]:


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
df = pd.DataFrame(columns=['lon', 'lat', 'alt', 'time'])
for point in data:
    df = df.append({'lon': point.longitude, 'lat' : point.latitude, 'alt' : point.elevation, 'time' : point.time}, ignore_index=True)
df.describe()


# In[ ]:


#Load the trained ML model
pkl_filename = "pickle_model.pkl"
with open(pkl_filename, 'rb') as file:
    
    MLmodel = pickle.load(file)


# In[ ]:


#Ingest user input into trained ML model
forest_predicted = MLmodel.predict(dfUserMLsub)

