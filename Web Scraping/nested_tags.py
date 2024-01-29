import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

boxes = soup.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")
print(len(boxes))

# getting only one box
box = soup.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")[3]
# print(box)

name = box.find('a')
print(name.string)

desc = box.find('p', class_="description card-text")
print(desc.string)
