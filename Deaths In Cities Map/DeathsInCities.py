import pandas
import folium

def DetermineRadius(num):
    if num > 1000:
        return 32
    elif num > 200:
        return 16
    elif num > 100:
        return 8
    elif num > 50:
        return 4
    else:
        return 2

def DetermineColor(num):
    if num > 1000:
        return 'black'
    elif num > 200:
        return 'red'
    elif num > 100:
        return 'orange'
    elif num > 50:
        return 'yellow'
    else:
        return 'green'

map = folium.Map(location = [37.5, -100], zoom_start = 6)
feature_group = folium.FeatureGroup(name = "Death Count")

data = pandas.read_csv("deaths2015data.csv")
week_44_data = data.set_index("MMWR_Week")
week_44_data = week_44_data.loc[44]
week_44_data = week_44_data.set_index("Reporting_Area")
week_44_data = week_44_data.drop(week_44_data.index[0:10], 0)

latitude = list(week_44_data["Latitude"])
longitude = list(week_44_data["Longitude"])
all_deaths = list(week_44_data["All_Causes_by_Age_Years_All_Ages"])

for lat, lon, ded in zip(latitude, longitude, all_deaths):
    feature_group.add_child(folium.CircleMarker(location = [lat, lon], radius = DetermineRadius(ded), fill = True,
                            color = DetermineColor(ded), fill_color = DetermineColor(ded),
                            popup = str(ded) + " deaths" ))

map.add_child(feature_group)
map.save("DeathsInCitiesWeek442015.html")
