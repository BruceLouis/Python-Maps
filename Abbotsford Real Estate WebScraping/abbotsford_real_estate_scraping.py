import requests
import pandas
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
from time import sleep

geolocator = Nominatim()

base_url_1 = "https://www.rew.ca/properties/areas/abbotsford-bc/page/"
base_url_2 = "?ajax=true"

initial_r = requests.get("https://www.rew.ca/properties/areas/abbotsford-bc/page/1?ajax=true")
initial_c = initial_r.content

initial_soup = BeautifulSoup (initial_c, "html.parser")

max_page = initial_soup.find_all("li", {"class": "paginator-last paginator-control"})

#list only has 1 item, so it has to be in index 0
max_page = max_page[0].find("a").get("href").split("?")

#splits into ['/properties..../page/25', 'ajax=true']
max_page = max_page[0].split("/")[-1]
print (max_page)

data_list = []

#for now we will do 4 pages of material
for page in range(1, int(max_page) - 20):
	r = requests.get(base_url_1 + str(page) + base_url_2)
	print(r)
	c = r.content

	soup = BeautifulSoup (c, "html.parser")
	all_items = soup.find_all("article", {"class": "displaypanel"})

	for items in all_items:
		#extract the url links of listing 
		links = items.find("a")
		links = links.get('href').split("?")
		links = "https://www.rew.ca" + links[0]
		print("links: " + links)
			
		address = items.find("div", {"class": "displaypanel-section"}).text.replace("\n"," ")
		if "-" in address:
			coord_address = address.split("-")
			coord_address = coord_address[1]
		else:
			coord_address = address
		
		coordinates = geolocator.geocode(str(coord_address))
		data_frames = {}
		data_frames["Price"] = items.find("div", {"class":"displaypanel-title visible-xs"}).text
		data_frames["Address"] = address
		'''
		for list_features in items.find_all("li", {"class":"listing-feature"}):    
			list_features = list_features.text.split()
			data_frames[list_features[1]] = list_features[0]
		'''
		data_frames["Webpage"] = links
			
		#obtain the coordinates for the address
		try:
			data_frames["Latitude"] = coordinates.latitude
			data_frames["Longitude"] = coordinates.longitude
		except:
			data_frames["Latitude"] = None
			data_frames["Longitude"] = None
		data_list.append(data_frames)
		
		#sleep is avoiding the 429 error to not overload the servers with request 
		sleep(20)
	
print(data_list) 
output = pandas.DataFrame(data_list)
output.to_csv("AbbotsfordRealEstate.csv")

