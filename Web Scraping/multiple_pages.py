import pandas as pd
import requests
# import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/search?q=mobile%20under%2050000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

response = requests.get(url)
# print(response)

soup = BeautifulSoup(response.text, "lxml")
# print(soup)
box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

Mobile_names = []
Mobile_prices = []
Mobile_descs = []
Mobile_reviews = []

names = box.find_all("div", class_="_4rR01T")
# print(names)

for name in names:
    i = name.text
    Mobile_names.append(i)

print(len(Mobile_names))

prices = box.find_all("div", class_="_30jeq3 _1_WHN1")
# print(prices)

for price in prices:
    i = price.text
    Mobile_prices.append(i)

print(len(Mobile_prices))

descs = box.find_all("ul", class_="_1xgFaf")
# print(descs)

for desc in descs:
    i = desc.text
    Mobile_descs.append(i)

print(len(Mobile_descs))

reviews = box.find_all("div", class_="_3LWZlK")
# print(reviews)

for review in reviews:
    i = review.text
    Mobile_reviews.append(i)

print(len(Mobile_reviews))

# completed till 19.00

# creating the dataframe
# df = pd.DataFrame()

















# for i in range(1,11):
#
#     url = "https://www.flipkart.com/search?q=mobile%20under%2050000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
#
#     response = requests.get(url)
#     # print(response)
#
#     soup = BeautifulSoup(response.text, "lxml")
#     # print(soup)
#
#     next_page = soup.find("a", class_="_1LKTO3").get("href")
#     # print(next_page)
#
#     next_page = next_page.removesuffix(next_page.split("=")[-1])
#
#     next_page += str(i)
#
#     complete_next_page = "https://www.flipkart.com" + next_page
#
#     print(complete_next_page)


