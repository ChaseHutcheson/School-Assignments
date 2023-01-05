import requests
import urllib.request
from pathlib import Path
import os
#API KEY: ojrrlXJErN3MvJrx6ddCMuLFPuKQfyGFUyuuYlbp

response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/opportunity/photos?sol=5000&camera=pancam&api_key=ojrrlXJErN3MvJrx6ddCMuLFPuKQfyGFUyuuYlbp")
request = response.request

directory = "All_School_Work\Projects\Python_APIs\\MarsImages"
os.mkdir(directory)

nasaAPI = response.json()
nasaPhotos = nasaAPI["photos"]

images = []
imageDates = []

for i in range(len(nasaPhotos)):
    data = nasaPhotos[i]
    images.append(data["img_src"])
    imageDates.append(data["earth_date"])

combinedData = []

sum = 1
for i in range(len(nasaPhotos)):
    combinedData.append({
        "Image Date" : imageDates[i],
        "Image" : urllib.request.urlretrieve(f"{images[i]}", f"All_School_Work\Projects\Python_APIs\\MarsImages\\MarsImage{sum}.JPG")
    })
    sum = sum + 1

print(combinedData)