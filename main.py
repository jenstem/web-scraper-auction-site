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