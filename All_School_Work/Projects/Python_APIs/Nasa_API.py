import requests
#API KEY: ojrrlXJErN3MvJrx6ddCMuLFPuKQfyGFUyuuYlbp

response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/opportunity/photos?sol=4000&camera=pancam&api_key=ojrrlXJErN3MvJrx6ddCMuLFPuKQfyGFUyuuYlbp")
request = response.request

print(response.json())