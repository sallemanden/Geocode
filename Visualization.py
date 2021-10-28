import pandas as pd
import folium
from folium.plugins import MarkerCluster

# DISPLAY THE MAP
map = folium.Map(location=[55.64152,12.08035], tiles ='OpenStreetMap', zoom_start = 13)

# CREATE A STATIC MARKER AT STATIC LOCATION
folium.Marker(location=[55.65233,12.13799], popup='POSTOFFICE', icon = folium.Icon(color='red')).add_to(map)

# READ THE CSV FILE
csv = pd.read_csv('locationGeo.csv')

# ILTERATE THROUGH THE CSV FILE AND ADD THE DATA TO THREE VARIABLES
for i, row in csv.iterrows():
    street = csv.at[i,'street']
    lat = csv.at[i,'lat']
    lng = csv.at[i,'lng']

    # CREATE A MARKER FOR EVERY ADDRESS IN THE CSV FILE
    folium.Marker(location=[lat,lng], popup=street, icon = folium.Icon(color='blue')).add_to(map)

# ADD THE MAP TO INDEX.HTML FILE
map.save('index.html')
