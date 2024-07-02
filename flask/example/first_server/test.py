import requests

response = requests.get("http://127.0.0.1:8080/test/json")
fruits = response.json()

for fruit in fruits:
  print(fruit)