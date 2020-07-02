# RateMyRun

#### Web-based application that provides a difficulty score based on route features. 

[About](https://docs.google.com/presentation/d/1c3w7a2jl3yOn5c4sGImYtmCMqDOdIV-y/edit#slide=id.p1)
[Demo](https://www.youtube.com/watch?v=VSw8FKZB6sc)

python libraries:
- scikit-learn
- requests
- streamlit
- pandas

## How it works
RateMyRun uses a Random Forest algorithm that is trained on existing descriptions of running trails around USA, webscaped from trailrunproject.com. It extracts relevant info (distance, location, elevation gain/loss, etc.) about a route from a provided .gpx file and makes a prediction of the difficulty based on similar routes that have been rated by the users. The result is a difficulty score of a new trail that allows new runners plan activities in new areas at an expected challenge.

You can use your favorite web or phone app to map a trail run. Save it to a .gpx file and upload it to [site]. 
