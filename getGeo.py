import pandas as pd
import requests
import json

# READ CSV FILE
csv = pd.read_csv("locations.csv")

# USE API RESPONSE TO FIND LATITUDE AND LONGITUDE
# ILTERATE THROUGH EVERY SINGLE ROW IN THE CSV FILE AND ADD TO LAT AND LNG
for i, row in csv.iterrows():
    address = str(csv.at[i,'street']) + ',' + str(csv.at[i,'zip']) + ',' + str(csv.at[i,'country'])

    parameters = {
        "key" : "btT47svcW8jcWNEAIAGNlrXgiv0Orxmw",
        "location" : address
    }
    response = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params = parameters)
    data = json.loads(response.text)['results']

    lng = data[0]['locations'][0]['latLng']['lng']
    lat = data[0]['locations'][0]['latLng']['lat']

    csv.at[i,'lng'] = lng
    csv.at[i,'lat'] = lat

 # CREATE A NEW CSV FILE WITH THE LONGITUDE AND LATITUDE
csv.to_csv('locationGeo.csv')
