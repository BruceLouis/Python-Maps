import pandas
import folium

def CreateMap(data_type):

    def CreateMarker(png_file_name, size):
        custom_icon = folium.CustomIcon(png_file_name, icon_size = (size, size))
        corrected_popup = folium.Popup(nam + ": " + str(mun) + ", " + str(cod), parse_html=True) #required to have folium read strings that have special characters like , and space by parsing html
        return folium.Marker(location = [lat, lon], popup = corrected_popup, icon = custom_icon)

    latitude = list(data_type["Latitude"])
    longitude = list(data_type["Longitude"])
    name = list(data_type["Name"])
    municipality = list(data_type["Municipality"])
    country_code = list(data_type["ISO_Country_Code"])
    airport_type = list(data_type["Type"])

    for lat, lon, nam, mun, cod, typ in zip(latitude, longitude, name, municipality, country_code, airport_type):
        if typ == "large_airport":
            feature_group_large_airport.add_child(CreateMarker("airplane-royal-blue.png", 25))
        elif typ == "medium_airport":
            feature_group_medium_airport.add_child(CreateMarker("airplane-baby-blue.png", 17))
        elif typ == "small_airport":
            feature_group_small_airport.add_child(CreateMarker("airplane-green.png", 12))
        elif typ == "heliport":
            feature_group_heliport.add_child(CreateMarker("helicopter-24.png", 12))
        elif typ == "seaplane_base":
            feature_group_seaplane_base.add_child(CreateMarker("seaplane-icon.png", 12))
        elif typ == "balloonport":
            feature_group_balloonport.add_child(CreateMarker("hot_air_balloon.png", 12))       
        else:
            feature_group.add_child(CreateMarker("closed-icon.png", 10))

def NameMap(html_file_name):

    map.add_child(feature_group)
    map.add_child(feature_group_balloonport)
    map.add_child(feature_group_heliport)
    map.add_child(feature_group_seaplane_base)
    map.add_child(feature_group_small_airport)
    map.add_child(feature_group_medium_airport)
    map.add_child(feature_group_large_airport)
    map.add_child(folium.LayerControl())
    map.save(html_file_name)    


data = pandas.read_csv("airportCodeData.csv")
sampled_data = data.sample(n = 1000) #since the data itself has 50k+ rows, gotta reduce the sample size to a reasonable number

asia_data = data.set_index("Continent")
asia_data = asia_data.loc["AS"]
sampled_asia_data = asia_data.sample(n = 1500)

map = folium.Map(location = [45, 20], zoom_start = 5)
feature_group_large_airport = folium.FeatureGroup(name = "Large Airports")
feature_group_medium_airport = folium.FeatureGroup(name = "Medium Airports")
feature_group_small_airport = folium.FeatureGroup(name = "Small Airports")
feature_group_heliport = folium.FeatureGroup(name = "Heliports")
feature_group_seaplane_base = folium.FeatureGroup(name = "Seaplane Base")
feature_group_balloonport = folium.FeatureGroup(name = "Hot Air Balloon Port")
feature_group = folium.FeatureGroup(name = "Closed")

CreateMap(sampled_data)
NameMap("AirportMap.html")

#resets the marker

map = folium.Map(location = [35, 110], zoom_start = 7, min_zoom = 4)
feature_group_large_airport = folium.FeatureGroup(name = "Large Airports")
feature_group_medium_airport = folium.FeatureGroup(name = "Medium Airports")
feature_group_small_airport = folium.FeatureGroup(name = "Small Airports")
feature_group_heliport = folium.FeatureGroup(name = "Heliports")
feature_group_seaplane_base = folium.FeatureGroup(name = "Seaplane Base")
feature_group_balloonport = folium.FeatureGroup(name = "Hot Air Balloon Port")
feature_group = folium.FeatureGroup(name = "Closed")

CreateMap(sampled_asia_data)
NameMap("AirportAsia.html")

