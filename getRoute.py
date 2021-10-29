import pandas as pd
import requests
import json

# # READ CSV FILE
df = pd.read_csv("locationGeo.csv")

#ILTERATE THROUGH EVERY ROW IN CSV FILE AND CALL API RESPONSE TO FIND DIRECTIONS
for i, row in df.iterrows():
    fromAddress = "Roskilde University"
    toAddress = str(df.at[i, 'street']) + ',' + str(df.at[i,'zip']) + ',' + str(df.at[i,'country'])

    parameters = {
        "key" : "btT47svcW8jcWNEAIAGNlrXgiv0Orxmw",
        "from" : fromAddress,
        "to" : toAddress
    }

    response = requests.get("http://www.mapquestapi.com/directions/v2/route", params = parameters)
    data = json.loads(response.text)
    print(data)
