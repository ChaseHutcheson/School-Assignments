#! NEED TO INSTALL LIBRARYS USING PIP - Beutiful Soup 4
#pip install bs4
from urllib import response
from bs4 import BeautifulSoup
from requests import get

url = "https://mahoningctc.com/mcctc-high-school-staff"
response = get(url)
# print(response.text)
#print(respons.text[:501])

soup = BeautifulSoup(response.text, 'html.parser')
#print(type(soup))
#print(soup)
teachers = soup.find_all('tr')
print(teachers)
for item in teachers:
    print(item.text)
