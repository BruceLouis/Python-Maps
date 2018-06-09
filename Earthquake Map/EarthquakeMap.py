import pandas
import folium

def PlaceMarker(magni):
    if magni < 1.0:
        size = 2
        colour = 'green'
    elif magni < 2.0:
        size = 4
        colour = 'yellow'
    elif magni < 3.0:
        size = 6
        colour = 'orange'
    elif magni < 4.0:
        size = 8
        colour = 'red'
    else:
        size = 12
        colour = 'black'
    return folium.CircleMarker(location = [lat,lon], radius = size,
                               color = colour, fill_opacity = 0.5, fill = True,
                               popup = folium.Popup(locale + ", Magnitude: " + str(magni), parse_html=True))

map = folium.Map(location = [45, 100], zoom_start = 4)

data = pandas.read_csv("all_month.csv")
sampled_data = data.sample(n = 1000)

level_1 = folium.FeatureGroup("Magnitude < 1.0")
level_2 = folium.FeatureGroup("Magnitude < 2.0")
level_3 = folium.FeatureGroup("Magnitude < 3.0")
level_4 = folium.FeatureGroup("Magnitude < 4.0")
level_5 = folium.FeatureGroup("Magnitude >= 4.0")

latitude = list(sampled_data["latitude"])
longitude = list(sampled_data["longitude"])
magnitude = list(sampled_data["mag"])
location = list(sampled_data["place"])

for lat, lon, mag, locale in zip(latitude, longitude, magnitude, location):
    if mag < 1.0:
        level_1.add_child(PlaceMarker(mag))
    elif mag < 2.0:
        level_2.add_child(PlaceMarker(mag))
    elif mag < 3.0:
        level_3.add_child(PlaceMarker(mag))
    elif mag < 4.0:
        level_4.add_child(PlaceMarker(mag))
    else:        
        level_5.add_child(PlaceMarker(mag))

map.add_child(level_1)
map.add_child(level_2)
map.add_child(level_3)
map.add_child(level_4)
map.add_child(level_5)
map.add_child(folium.LayerControl())
map.save("EarthquakeMap.html")
