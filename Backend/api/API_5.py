import requests
import json

url = input("Enter url: ")

r = requests.get(url)

print(r.json())
