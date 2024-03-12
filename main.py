import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.iplt20.com/auction"
r = requests.get(url)

# Test if website is accessible or not by uncommenting first
# print(r)

soup = BeautifulSoup(r.text, "html.parser")