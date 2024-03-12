import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.iplt20.com/auction"
r = requests.get(url)

# Test if website is accessible or not by uncommenting first
# print(r)

soup = BeautifulSoup(r.text, "html.parser")

# Titles of the columns
table = soup.find("table",class_ = "ih-td-tab auction-tbl")
header = table.find_all("th")

titles = []

for i in header:
    title = i.text
    titles.append(title)

df = pd.DataFrame(columns = titles)

# Details of the auction
rows = table.find_all("tr")
print(rows)

for i in rows[1:]:
    first_td = i.find_all("td")[0].find("div",class_ = "ih-pt-ic").text.strip()
    data = i.find_all("td")[1:]
    row = [tr.text for tr in data]
    row.insert(0,first_td)
    l = len(df)
    df.loc[l] = row