from urllib import response
from bs4 import BeautifulSoup
from requests import get

url = "https://twitter.com/elonmusk"
response = get(url)
# print(response.text)
#print(respons.text[:501])

soup = BeautifulSoup(response.text, 'html.parser')
#print(type(soup))
#print(soup)
elons_tweets = soup.find_all('span', {"class": "css-1dbjc4n"})
print(elons_tweets)

#for item in elons_tweets:
#    print(item.text)
