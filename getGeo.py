import pandas as pd
import requests
import json

df = pd.read_csv("restaurants.csv")
pd.set_option('display.max_rows', None)

for i, row in df.iterrows():
    apiAddress = str(df.at[i,'street'])+','+str(df.at[i,'zip'])+','+str(df.at[i,'city'])+','+str(df.at[i,'country'])
    
    parameters = {
        "key": "enter your mapquestapi key here",
        "location": apiAddress
    }

    response = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params=parameters)
    print(response)
    data = response.text
    dataJ = json.loads(data)['results']
    lat = (dataJ[0]['locations'][0]['latLng']['lat'])
    lng = (dataJ[0]['locations'][0]['latLng']['lng'])
    
    df.at[i,'lat'] = lat
    df.at[i,'lng'] = lng
    
df.to_csv('restaurants_geo.csv')
