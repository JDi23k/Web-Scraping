import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.iplt20.com/auction/2022"

response = requests.get(url)
# print(response)

soup = BeautifulSoup(response.text, "lxml")

table = soup.find("table", class_="ih-td-tab auction-tbl")
# print(table)

# header
headers = table.find_all("th")

# fetching the headers of the table
titles = []
for header in headers:
    i = header.text
    titles.append(i)

# print(titles)

# creating the dataframe
df = pd.DataFrame(columns=titles)
# print(df)

rows = table.find_all("tr")
# print(rows)

# fetching all the rows of the table
for i in rows[1:]:
    data = i.find_all("td")
    row = [tr.text for tr in data]
    index = len(df)
    df.loc[index] = row

# print(df)

# removing the spaces
df['TEAM'] = df['TEAM'].str.strip()

# after removing the spaces
# print(df)

# saving the dataframe as a csv file
df.to_csv("IPL_auction_stats_2022.csv", index=False)
