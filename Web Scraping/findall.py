import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

prices = soup.find_all('h4', class_="float-end price card-title pull-right")
print(prices)
for price in prices:
    print(price.text)

descs = soup.find_all('p', class_="description card-text")
print(descs)
for desc in descs:
    print(desc.text)
