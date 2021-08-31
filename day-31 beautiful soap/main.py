from bs4 import BeautifulSoup
import requests

response = requests.get("https://letsboost.net/")

file = open("car.html")
data = file.read()
soup = BeautifulSoup(response.text,"html.parser")

print(soup.h1.text)

file.close()
