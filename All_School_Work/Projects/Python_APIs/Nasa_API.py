import requests
#API KEY: ojrrlXJErN3MvJrx6ddCMuLFPuKQfyGFUyuuYlbp

response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/opportunity/photos?sol=4000&camera=pancam&api_key=ojrrlXJErN3MvJrx6ddCMuLFPuKQfyGFUyuuYlbp")
request = response.request

nasaAPI = response.json()
nasaPhotos = nasaAPI["photos"]

images = []
imageDates = []

for i in range(len(nasaPhotos)):
    data = nasaPhotos[i]
    images.append(data["img_src"])
    imageDates.append(data["earth_date"])

combinedData = []

for i in range(len(nasaPhotos)):
    combinedData.append({
        "imgLink" : images[i],
        "imgDate" : imageDates[i] 
    })

print(combinedData)