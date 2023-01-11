# Import libraries
from bs4 import BeautifulSoup
import requests
import csv
 
# Set the URL to scrape | Works as Intended
url = "https://weather.com/weather/tenday/l/USCA0987:1:US"
 
# Send a GET request to the URL and store the response | Works as Intended
response = requests.get(url)
 
# Parse the response using BeautifulSoup | Works as intended
soup = BeautifulSoup(response.text, "html.parser")
 
# Find the forecast container element | Class mentioned doesn't exist. Replaced With "DailyForecast--DisclosureList--nosQS"
forecast_container = soup.find(class_="DailyForecast--DisclosureList--nosQS")
 
# Create an empty list to store the forecast data | To make code below work, I removed the "forcast_data" list and made each data piece their own list
forecast_dates = []
forecast_description = []
forecast_hi = []
forecast_lo = []
 
# Loop through each row in the forecast table | There isnt a single table that holds all the data, so we cant loop through one.
# Instead I will first find the classes of all the data
forcast_date_data = forecast_container.find_all(class_="DetailsSummary--daypartName--kbngc")

forcast_description_data = forecast_container.find_all(class_="DailyContent--narrative--3Ti6_")

forcast_hi_data = forecast_container.find_all(class_="DetailsSummary--highTempValue--3PjlX")

forcast_lo_data = forecast_container.find_all(class_="DetailsSummary--lowTempValue--2tesQ")

# Then, I will loop through all the HTML, extract the text and append that text into their own list like in the 2 for loops below
for text in forcast_date_data:
  forecast_dates.append(text.text)

for text in forcast_description_data:
  forecast_description.append(text.text)

# In the 2 for loops below, The HTML text is extracted, the degree symbol is removed and the added to the list
for text in forcast_hi_data:
  hi_temp = text.text
  hi_temp = hi_temp.replace("°", "")
  forecast_hi.append(hi_temp)

for text in forcast_lo_data:
  lo_temp = text.text
  lo_temp = lo_temp.replace("°", "")
  forecast_lo.append(lo_temp)

print(forecast_dates)
print(forecast_description)
print(forecast_hi)
print(forecast_lo)
 
# Open a new file to write the forecast data to | Works as Intended except I changed the file destination
with open("All_School_Work\\Projects\\ChatGPT3\\forecast.csv", "w") as csv_file:
  # Create a CSV writer | Works as Intended
  writer = csv.DictWriter(csv_file, fieldnames=["date", " description", " high", " low"])
 
  # Write the column headers | Works as intended
  writer.writeheader()
 
  # Write the forecast data to the file | Here, since the code abovve was different, I had to write a dictionary per row with a space between the commas to make it more ledgeable
  for i in range(len(forecast_dates)):
    writer.writerow({"date": forecast_dates[i], " description": " " + forecast_description[i], " high": " " + forecast_hi[i], " low": " " + forecast_lo[i]})