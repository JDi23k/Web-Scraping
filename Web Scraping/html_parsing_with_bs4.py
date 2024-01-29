import requests
from bs4 import BeautifulSoup

# url = "https://courses.wscubetech.com/"
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
response = requests.get(url)
#print(response)

soup = BeautifulSoup(response.text,"lxml")
print(soup)