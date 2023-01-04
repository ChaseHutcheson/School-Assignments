import requests

response = requests.get("https://api.thedogapi.com/v1/breeds/")
request = response.request

print(response.status_code)
print(response.text)
print(response.headers)
print(request.headers)