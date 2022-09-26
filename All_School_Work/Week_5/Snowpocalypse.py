import os
import requests
from bs4 import BeautifulSoup
import re
#Clears Terminal
os.system('cls')

#Data List
all_data = []

#Scrapes the data
req = requests.get("https://www.msn.com/en-us/weather/forecast/in-?loc=eyJ0IjoxLCJ4IjotODAuNjY1LCJ5Ijo0MS4wMzJ9&ocid=ansmsnweather")
soup = BeautifulSoup(req.content, "html.parser")

#appends only text from data
temp_nums = soup.get_text()
pattern = "[1-9]+"

x = (re.findall(pattern, temp_nums))

for i in range(len(x)):
    if int(x[i]) > 100:
        all_data.append(x[i])

print(all_data)