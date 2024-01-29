import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://ticker.finology.in/"

response = requests.get(url)
# print(response)

soup = BeautifulSoup(response.text, "lxml")

table = soup.find("table", class_="table table-sm table-hover screenertable")
# print(table)

headers = table.find_all('th')
# print(headers)
titles = []
for header in headers:
    i = header.text
    titles.append(i)

# print(titles)

# creating the dataframe
df = pd.DataFrame(columns=titles)

rows = table.find_all("tr")
# print(rows)

for i in rows[1:]:
    data = i.find_all("td")
    row = [tr.text for tr in data]
    # print(row)
    index = len(df)
    df.loc[index] = row

print(df)

df['Company'] = df['Company'].str.strip()

# after removing the spaces
print(df)

# saving the dataframe as a csv file
df.to_csv("stock_market.csv", index=False)
