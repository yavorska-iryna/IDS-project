# RateMyRun

#### Web-based application that provides a difficulty score based on route features. 

[About](https://docs.google.com/presentation/d/1c3w7a2jl3yOn5c4sGImYtmCMqDOdIV-y/edit#slide=id.p1)

Input: .gpx file

## How it works
RateMyRun uses a Random Forest algorithm that is trained on existing descriptions of running trails around USA, webscaped from trailrunproject.com. It extracts important information about a route from a provided .gpx file and makes a prediction of the difficulty based on similar routes that have been rated by the users. The result is a difficulty score of a new trail that allows new runners plan activities in new areas at an expected challenge.

