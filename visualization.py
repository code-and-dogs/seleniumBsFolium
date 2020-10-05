import pandas as pd
import folium
from folium import FeatureGroup
from folium.plugins import MarkerCluster

#Create the base Map
m = folium.Map(location=[48.86762,2.3624], tiles='OpenStreetMap', zoom_start=5)

#Read the data
df = pd.read_csv("restaurants_geo.csv")

#Create the markers
markerCluster = MarkerCluster().add_to(m)
for i, row in df.iterrows():
    lat = df.at[i,'lat']
    lng = df.at[i,'lng']

    restaurant = df.at[i,'restaurant']
    popup = df.at[i,'restaurant'] +'<br>' + str(df.at[i, 'street']) +'<br>' + str(df.at[i, 'zip'])

    if restaurant == 'McDonalds':
        color = 'blue'
    else:
        color = 'red'

    folium.Marker(location=[lat, lng],popup=restaurant, icon=folium.Icon(color=color)).add_to(markerCluster)

m.save("index.html")