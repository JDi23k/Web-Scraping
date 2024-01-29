import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")
print(soup.div) # to get only the div tag from the html