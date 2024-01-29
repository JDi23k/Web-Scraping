import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

names = soup.find_all('a', class_="title")
# print(names)

product_name = []
for name in names:
    i = name.text
    product_name.append(i)

print(product_name)

prices = soup.find_all('h4', class_="float-end price card-title pull-right")
# print(prices)

prices_list = []
for price in prices:
    i = price.text
    prices_list.append(i)

print(prices_list)

descs = soup.find_all('p', class_="description card-text")
# print(descs)

description_list = []
for desc in descs:
    i = desc.text
    description_list.append(i)

print(description_list)

reviews = soup.find_all("p", class_ = "float-end review-count")
# print(reviews)

review_list = []
for review in reviews:
    i = review.text
    review_list.append(i)

print(review_list)

# Creating the dataframe
df = pd.DataFrame({"Product Name":product_name, "Price":prices_list, "Description":description_list, "Reviews":review_list})

# saving it as a csv file
df.to_csv("Product_details.csv", index = False)

# saving it as a excel file
df.to_excel("Product_details.xlsx", index=False)


