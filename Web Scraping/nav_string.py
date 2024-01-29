import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone"
response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

tag = soup.header.div.a.button.span
print(tag.string)
