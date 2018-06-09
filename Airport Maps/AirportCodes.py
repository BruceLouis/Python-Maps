import pandas
import folium

def CreateMap(data_type, html_file_name, lat_start, lon_start, zoom_begin, zoom_bound = 1):

    def CreateMarker(png_file_name, size):
        custom_icon = folium.CustomIcon(png_file_name, icon_size = (size, size))
        corrected_popup = folium.Popup(nam + ": " + str(mun) + ", " + str(cod), parse_html=True) #required to have folium read strings that have special characters like , and space by parsing html
        return folium.Marker(location = [lat, lon], popup = corrected_popup, icon = custom_icon)
        
    map = folium.Map(location = [lat_start, lon_start], zoom_start = zoom_begin, min_zoom = zoom_bound)
    feature_group_large_airport = folium.FeatureGroup(name = "Large Airports")
    feature_group_medium_airport = folium.FeatureGroup(name = "Medium Airports")
    feature_group_small_airport = folium.FeatureGroup(name = "Small Airports")
    feature_group_heliport = folium.FeatureGroup(name = "Heliports")
    feature_group_seaplane_base = folium.FeatureGroup(name = "Seaplane Base")
    feature_group_balloonport = folium.FeatureGroup(name = "Hot Air Balloon Port")
    feature_group = folium.FeatureGroup(name = "Closed")

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
                
    map.add_child(feature_group)
    map.add_child(feature_group_balloonport)
    map.add_child(feature_group_heliport)
    map.add_child(feature_group_seaplane_base)
    map.add_child(feature_group_small_airport)
    map.add_child(feature_group_medium_airport)
    map.add_child(feature_group_large_airport)
    map.add_child(folium.LayerControl())
    map.save(html_file_name)
    
 
data = pandas.read_csv("airportCodeData.csv", keep_default_na = False)
sampled_data = data.sample(n = 1000) #since the data itself has 50k+ rows, gotta reduce the sample size to a reasonable number

#extract individual continental data
continental_data = data.set_index("Continent")
asia_data = continental_data.loc["AS"]
europe_data = continental_data.loc["EU"]
north_america_data = continental_data.loc["NA"]
sampled_asia_data = asia_data.sample(n = 1500)
sampled_europe_data = europe_data.sample(n = 1500)
sampled_north_america_data = north_america_data.sample(n = 1500)

CreateMap(sampled_data, "AirportMap.html", 45, 20, 5)
CreateMap(sampled_asia_data, "AirportAsia.html", 35, 110, 7, 4)
CreateMap(sampled_europe_data, "AirportEU.html", 45, 20, 7, 4)
CreateMap(sampled_north_america_data, "AirportNA.html", 45, -110, 7, 4)
