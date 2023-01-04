from time import sleep
from urllib import response
from bs4 import BeautifulSoup
from requests import get
import os
import tweepy
#Twitter Dev Keys
Twitter_Api_Key = "QobijQVn3b3aBl3Iblrm6YOwA"
Twitter_Api_Key_Secret = "Xj1FoctEqHyAiS0TFTkmwl4NUz5tXyjhmDkvDrg8uGmaf1euDQ"
Twitter_Bearer_Token = "AAAAAAAAAAAAAAAAAAAAAGZahgEAAAAAGRI%2BlUbSf%2FOE64od1NUFrqszl3Q%3D02oOXKtSitqp7ITEMzaacYEHnzGEUoThV8AFdu3cL31WMsIO85"

#Clears Terminal
os.system('cls')

#list to store temps
temp_days_list = []
temps_list = []
new_temps_list = []
precip_list = []
new_precip_list = []
final_Sentences = []

#Url
url = "https://weather.com/weather/tenday/l/08bd50a1176f54984872ff805fdff0dff19c2d1543f8aa72dc2f88ccd6c538d9#detailIndex5"
response = get(url)

#Function to pull HTML
soup = BeautifulSoup(response.text, 'html.parser')

#Pulls Data
temp_days = soup.find_all("h3", {"DetailsSummary--daypartName--2FBp2"})

temps = soup.find_all("div", {"class": "DetailsSummary--temperature--1Syw3"})

precip = soup.find_all("div", {"class": "DetailsSummary--precip--1ecIJ"})

#Appends all data to lists
for item in temp_days:
    temp_days_list.append(item.text)

for item in temps:
    temps_list.append(item.text)

for item in precip:
    precip_list.append(item.text)

for i in range(len(temps_list)):
    new_temps = str(temps_list[i]).split("/")
    new_temps_list.append(new_temps)

for i in range(len(precip_list)):
    new_precip = str(precip_list[i]).split("Rain")
    new_precip_list.append(new_precip)

#Prints all dates and temps and reain chances
for i in range(len(temp_days)):
    if i == 0:
        final_Sentences.append(f"{temp_days_list[i]}, The tempurature is going to be a high of {new_temps_list[i][0]} degrees with a low of {new_temps_list[i][1]} and a {new_precip_list[i][1]} chance of Rain")
    if  i > 0:
        final_Sentences.append(f" On {temp_days_list[i]}, The tempurature is going to be a high of {new_temps_list[i][0]} degrees with a low of {new_temps_list[i][1]} and a {new_precip_list[i][1]} chance of Rain")
    
# auth = tweepy.OAuthHandler("TUDlkN5VLnLRBxZQXgfGAP6wn", "exOIcTdVcdhgCysqLzy6Bk403TUw1htQXIsWVtkbhAS5YUgPj5")
# auth.set_access_token("1575153918291517440-31zRsR6Kt7Pjfvu8qb5YmHtW9pDN7I", "weYfuAwGNsIbAaJJcI6FPmNA3m4hJjM4E8mE6RQicu14p")

# #Create API object
# api = tweepy.API(auth)

# #Create a tweet
# #api.update_status(final_Sentences[1])
# #sleep(60)
# #api.update_status(final_Sentences[2])
 
print(final_Sentences)