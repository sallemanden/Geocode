import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Start the map at center of roskilde
m = folium.Map(location=[55.64152,12.08035], tiles ='OpenStreetMap', zoom_start = 13)

# Install one static marker as Post Office, we do not have this location in our  locationGeo.csv since we are adding new post officies
folium.Marker(location=[55.65233,12.13799], popup='POSTHUS', icon = folium.Icon(color='red')).add_to(m)

# read the location geo CSV file
csv = pd.read_csv('locationGeo.csv')

# Go over every single row in our CSV file and take latitude and longitiude as well as street
for i, row in csv.iterrows():
    street = csv.at[i,'street']
    lat = csv.at[i,'lat']
    lng = csv.at[i,'lng']

    # Use the above mentioned variables to create a marker on the map, latitude and longitiude is used to determine the location, while street gives valueable information.
    folium.Marker(location=[lat,lng], popup=street, icon = folium.Icon(color='blue')).add_to(m)

# save the markers in the index.html which is where we display the map.
m.save('index.html')
