import folium
import pandas
import re
from geopy.geocoders import Nominatim

def CreateMarker(color):
    return folium.Marker(location = [lat, lon], popup = cost + " " + add + " " + web,
                         icon = folium.Icon(color = color))

data = pandas.read_csv("AbbotsfordRealEstate.csv")
geolocator = Nominatim()
map = folium.Map(location = [49.0504, -122.3045], zoom_start = 15)

under_200k = folium.FeatureGroup(name = "Under 200k")
under_300k = folium.FeatureGroup(name = "Under 300k")
the_rest = folium.FeatureGroup(name = "The Rest")
address_list = list(data["Address"])

latitude = list(data["Latitude"])
longitude = list(data["Longitude"])
price = list(data["Price"])
address = list(data["Address"])
webpage = list(data["Webpage"])

for lat, lon, cost, add, web in zip(latitude, longitude, price, address, webpage):
    new_cost = re.sub('[^a-zA-Z0-9 \n\.]', '', cost) #rids the dollar sign and the comma
    try:
        if float(new_cost) < 200000:
            under_200k.add_child(CreateMarker('green'))
        elif float(new_cost) < 300000:
            under_300k.add_child(CreateMarker('blue'))
        else:
            the_rest.add_child(CreateMarker('red'))
    except:
        pass

map.add_child(under_200k)
map.add_child(under_300k)
map.add_child(the_rest)
map.add_child(folium.LayerControl())
map.save("AbbotsfordHousingMap.html")
