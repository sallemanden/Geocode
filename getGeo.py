import pandas as pd
import requests
import json

#Read CSV file
df = pd.read_csv("locations.csv")


# Loop through every single row of the CSV file, take street, zip and country as the apiAddress we utilize as parameter
for i, row in df.iterrows():
    address = str(df.at[i,'street']) + ',' + str(df.at[i,'zip']) + ',' + str(df.at[i,'country'])

    parameters = {
    # location is = to the variable since we loop through our csv file
        "key" : "btT47svcW8jcWNEAIAGNlrXgiv0Orxmw",
        "location" : address
    }
    # Only get latitude and longitiude
    response = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params = parameters)
    data = json.loads(response.text)['results']

    lng = data[0]['locations'][0]['latLng']['lng']
    lat = data[0]['locations'][0]['latLng']['lat']


    df.at[i,'lat'] = lat
    df.at[i,'lng'] = lng

 # Make a new CSV File with the latitude and longitiude values
df.to_csv('locationGeo.csv')
