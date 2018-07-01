import requests
import pandas
from bs4 import BeautifulSoup

base_url_1 = "https://www.rew.ca/properties/areas/abbotsford-bc/sort/featured/desc/page/"
base_url_2 = "?ajax=true"

initial_r = requests.get("https://www.rew.ca/properties/areas/abbotsford-bc/sort/featured/desc/page/1?ajax=true")
initial_c = initial_r.content

initial_soup = BeautifulSoup (initial_c, "html.parser")

max_page = initial_soup.find_all("div", {"class": "paginator"})
max_page = max_page[0].find_all("li", {"class": "paginator-page"})[-1].text

print(max_page)
data_list = []

for page in range(1, int(max_page)):
    r = requests.get(base_url_1 + str(page) + base_url_2)
    c = r.content

    soup = BeautifulSoup (c, "html.parser")
    all_items = soup.find_all("div", {"class": "row listing-row"})
    
    for items in all_items:
        data_frames = {}
        data_frames["Price"] = items.find("div", {"class":"listing-price"}).text
        data_frames["Address"] = items.find("span", {"class": "listing-address"}).find("a").text.replace("\n","")
        for list_features in items.find_all("li", {"class":"listing-feature"}):    
            list_features = list_features.text.split()
            data_frames[list_features[1]] = list_features[0]
        data_frames["Property Type"] = items.find("dd").text
        data_list.append(data_frames)

output = pandas.DataFrame(data_list)
output.to_csv("AbbotsfordRealEstateJune2018.csv")
