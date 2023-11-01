import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect

oyo_url = "https://www.oyorooms.com/hotels-in-jaipur"

req = requests.get(oyo_url)
content = req.content

soup = BeautifulSoup(content,"html.parser")

all_hotels = soup.find_all("div",{"class":"hotelCardListing"})

for hotel in all_hotels:
    hotel_dict = {}
    hotel_["name"] = hotel.find("h3",{"class":"ListingHotelDescription_hotelName"}).text
    hotel_["address"] = hotel.find("span",{"itemprop":"streetAddress"}).text
    hotel_dict["price"] = hotel.find("span",{"class":"ListingPrice__finalPrice"}).text

    try:
        hotel_dict["rating"] = hotel.find("span",{"class":"hotelRating__ratingSummary"}).text
    except AttributeError:
        hotel_dict["rating"] = None

    parent_amenities_element = hotel.find("div",{"class":"amenityWrapper"})

    amenities_list = []
    for  amenity in parent_amenities_element.find_all("div",{"class":"amenityWrapper__amenity"}):
        amenities_list.append(amenity.find("span",{"class":"d-body-sm"}).text.strip())

    hotel_dict["amenities"] = ', '.join(amenities_list[:-1])

    scraped_info_list.append(hotel_dict)
    connect.insert_into_table(args.dbname, tuple(hotel_dict.values()))

dataFrame = pandas.DataFrame(scraped_info_list)
print("createing csv file.....")
dataFrame.to_csv("oyo.csv")
