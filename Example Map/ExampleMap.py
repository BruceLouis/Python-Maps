import pandas
import folium

def GiveColor(el):
    if el > 3000:
        return 'orange'
    elif el > 2000:
        return 'yellow'
    else:
        return 'green' 

map = folium.Map(location = [45, -121], zoom_start = 5)
feature_group_volcanoes = folium.FeatureGroup(name = "Volcanoes")
feature_group_population = folium.FeatureGroup(name = "Population")

volcanoData = pandas.read_csv("Volcanoes_USA.txt")
latitude = list(volcanoData["LAT"])
longitude = list(volcanoData["LON"])
location = list(volcanoData["LOCATION"])
elevation = list(volcanoData["ELEV"])


feature_group_population.add_child(folium.GeoJson(data = open("world.json", "r", encoding = "utf-8-sig").read(),
style_function = lambda x: {"fillColor":"green" if x['properties']['POP2005'] < 10000000
                            else "orange" if x['properties']['POP2005'] < 100000000
                            else "red"} ))

for lat, lon, loc, elev in zip(latitude, longitude, location, elevation):
    feature_group_volcanoes.add_child(folium.CircleMarker(location = [lat, lon], radius = 8, popup = loc + ": " + str(elev) + " m",
    fill = True, fill_opacity = 0.75, fill_color = GiveColor(elev), color = GiveColor(elev)))
    
map.add_child(feature_group_population)
map.add_child(feature_group_volcanoes)
map.add_child(folium.LayerControl())
    
map.save("ExampleMap.html")
