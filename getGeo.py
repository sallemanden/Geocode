import pandas as pd
import requests
import json

#Read CSV file
csv = pd.read_csv("locations.csv")


# Loop through every single row of the CSV file, take street, zip and country as the apiAddress we utilize as parameter
for i, row in csv.iterrows():
    address = str(csv.at[i,'street']) + ',' + str(csv.at[i,'zip']) + ',' + str(csv.at[i,'country'])

    parameters = {
    # location is = to the variable since we loop through our csv file
        "key" : "btT47svcW8jcWNEAIAGNlrXgiv0Orxmw",
        "location" : address
    }
    # Only get latitude and longitiude
    resp = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params = parameters)
    data = json.loads(resp.text)['results']

    lng = data[0]['locations'][0]['latLng']['lng']
    lat = data[0]['locations'][0]['latLng']['lat']


    csv.at[i,'lat'] = lat
    csv.at[i,'lng'] = lng

 # Make a new CSV File with the latitude and longitiude values
csv.to_csv('locationGeo.csv')
