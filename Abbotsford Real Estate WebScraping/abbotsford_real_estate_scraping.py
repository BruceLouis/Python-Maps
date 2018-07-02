import requests
import pandas
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
from time import sleep

geolocator = Nominatim()

base_url_1 = "https://www.rew.ca/properties/areas/abbotsford-bc/sort/featured/desc/page/"
base_url_2 = "?ajax=true"

initial_r = requests.get("https://www.rew.ca/properties/areas/abbotsford-bc/sort/featured/desc/page/1?ajax=true")
initial_c = initial_r.content

initial_soup = BeautifulSoup (initial_c, "html.parser")

max_page = initial_soup.find_all("div", {"class": "paginator"})
max_page = max_page[0].find_all("li", {"class": "paginator-page"})[-1].text

print(max_page)
data_list = []

#to do, add a link to dataframe to the listing page
for page in range(1, int(max_page)):
    r = requests.get(base_url_1 + str(page) + base_url_2)
    c = r.content

    soup = BeautifulSoup (c, "html.parser")
    all_items = soup.find_all("div", {"class": "row listing-row"})
    
    for items in all_items:
        #extract the url links of listing 
        links = items.find("a")
        links = links.get('href').split("?")
        links = "https://www.rew.ca" + links[0]
        address = items.find("span", {"class": "listing-address"}).find("a").text.replace("\n","")
        if "-" in address:
            coord_address = address.split("-")
            coord_address = coord_address[1]
        else:
            coord_address = address
            
        coordinates = geolocator.geocode(coord_address + " Abbotsford")
        data_frames = {}
        data_frames["Price"] = items.find("div", {"class":"listing-price"}).text
        data_frames["Address"] = address
        for list_features in items.find_all("li", {"class":"listing-feature"}):    
            list_features = list_features.text.split()
            data_frames[list_features[1]] = list_features[0]
        data_frames["Webpage"] = links
        
        #obtain the coordinates for the address
        try:
            data_frames["Latitude"] = coordinates.latitude
            data_frames["Longitude"] = coordinates.longitude
        except:
            data_frames["Latitude"] = None
            data_frames["Longitude"] = None
        data_list.append(data_frames)
        sleep(20)
       
output = pandas.DataFrame(data_list)
output.to_csv("AbbotsfordRealEstate.csv")

