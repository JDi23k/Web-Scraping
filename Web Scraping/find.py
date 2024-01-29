# find - only for first div class
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

# print(soup.find('div'))
price = soup.find('h4', {"class": "float-end price card-title pull-right"})
print(price.string)

desc = soup.find('p', {"class": "description card-text"})
print(desc.string)

# another way to mention the class
desc1 = soup.find('p', class_="description card-text")
print(desc1.string)
