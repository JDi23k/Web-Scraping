import requests
from bs4 import BeautifulSoup
import re

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")
#data = soup.find_all(string="Galaxy Tab")
data = soup.find_all(string=re.compile("Galaxy"))
print(data)
