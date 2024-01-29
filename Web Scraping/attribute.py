import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")
#tag = soup.div # div tag
tag = soup.header # header tag
attributes = (tag.attrs)
print(attributes)
