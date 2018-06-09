import pandas
import folium

def CreateMarker(png_file_name, municipal, size):
    custom_icon = folium.CustomIcon(png_file_name, icon_size = (size, size))
    municipal = ''.join(e for e in str(municipal) if e.isalnum()) #getting rid of special characters 
    return folium.Marker(location = [lat, lon], popup = str(municipal) + ", " + str(cod), icon = custom_icon)

map = folium.Map(location = [45, 20], zoom_start = 5)
feature_group_large_airport = folium.FeatureGroup(name = "Large Airports")
feature_group_medium_airport = folium.FeatureGroup(name = "Medium Airports")
feature_group_small_airport = folium.FeatureGroup(name = "Small Airports")
feature_group_heliport = folium.FeatureGroup(name = "Heliports")
feature_group_seaplane_base = folium.FeatureGroup(name = "Seaplane Base")
feature_group_balloonport = folium.FeatureGroup(name = "Hot Air Balloon Port")
feature_group = folium.FeatureGroup(name = "Closed")

data = pandas.read_csv("airportCodeData.csv")
sampled_data = data.sample(n = 1000) #since the data itself has 50k+ rows, gotta reduce the sample size to a reasonable number

latitude = list(sampled_data["Latitude"])
longitude = list(sampled_data["Longitude"])
municipality = list(sampled_data["Municipality"])
country_code = list(sampled_data["ISO_Country_Code"])
airport_type = list(sampled_data["Type"])

for lat, lon, mun, cod, typ in zip(latitude, longitude, municipality, country_code, airport_type):
    if typ == "large_airport":
        feature_group_large_airport.add_child(CreateMarker("airplane-royal-blue.png", mun, 25))
    elif typ == "medium_airport":
        feature_group_medium_airport.add_child(CreateMarker("airplane-baby-blue.png", mun, 17))
    elif typ == "small_airport":
        feature_group_small_airport.add_child(CreateMarker("airplane-green.png", mun, 12))
    elif typ == "heliport":
        feature_group_heliport.add_child(CreateMarker("helicopter-24.png", mun, 12))
    elif typ == "seaplane_base":
        feature_group_seaplane_base.add_child(CreateMarker("seaplane-icon.png", mun, 12))
    elif typ == "balloonport":
        feature_group_balloonport.add_child(CreateMarker("hot_air_balloon.png", mun, 12))       
    else:
        feature_group.add_child(CreateMarker("closed-icon.png", mun, 10))
    
map.add_child(feature_group)
map.add_child(feature_group_heliport)
map.add_child(feature_group_seaplane_base)
map.add_child(feature_group_small_airport)
map.add_child(feature_group_medium_airport)
map.add_child(feature_group_large_airport)
map.add_child(folium.LayerControl())
map.save("AirportMap.html")
