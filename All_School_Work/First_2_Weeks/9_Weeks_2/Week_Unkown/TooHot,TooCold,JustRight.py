from bs4 import BeautifulSoup
import requests

url = "https://www.google.com/search?q="+"weather%20"+ " Canfield"
html = requests.get(url).content

soup = BeautifulSoup(html, 'html.parser')

temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
temp = temp.split("°F")

if int(temp[0]) >= 90:
    print(f"The current temp is {temp[0]} and that is too hot")

elif int(temp[0]) >= 65:
    print(f"The current temp is {temp[0]} and that is just right")
else:
    print(f"The current temp is {temp[0]} and that is too cold")