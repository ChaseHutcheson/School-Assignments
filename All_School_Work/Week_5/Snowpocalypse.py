import os
import requests
from bs4 import BeautifulSoup
#Clears Terminal
os.system('cls')

#Data List
all_data = []

#Scrapes the data
req = requests.get("https://www.msn.com/en-us/weather/forecast/in-?loc=eyJ0IjoxLCJ4IjotODAuNjY1LCJ5Ijo0MS4wMzJ9&ocid=ansmsnweather")
soup = BeautifulSoup(req.content, "html.parser")

#appends only text from data
all_data.append(soup.get_text())

for i in range(len(all_data)):
    possible_temps = 0
    numbers = all_data.find(str(possible_temps))
    all_data.append(numbers)
    possible_temps = possible_temps + 1

print(all_data)