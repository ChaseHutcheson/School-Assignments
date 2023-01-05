import requests
from pathlib import Path

query = input("Enter the book you want to search for: ")

response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={query}")

results = response.json()
results = results["items"]

resultsList = []

for i in range(len(results)):
    bookInfo = results[i]
    bookInfo = bookInfo["volumeInfo"]
    if bookInfo.__contains__("description") == True:
        resultsList.append({
        "Title" : bookInfo["title"],
        "Publish Date" : bookInfo["publishedDate"],
        "Description" : bookInfo["description"]
        })
    else:
        resultsList.append({
        "Title" : bookInfo["title"],
        "Publish Date" : bookInfo["publishedDate"],
        "Description" : "No Description Found"
        })

Path(f"All_School_Work\Projects\Python_APIs\\{query.upper()}.txt").write_text(str(resultsList).replace("\\", ""))