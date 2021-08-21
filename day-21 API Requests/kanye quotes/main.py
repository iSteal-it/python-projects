import requests

response = requests.get(url="https://api.kanye.rest/")
data = response.json()
print(data["quote"])
