import requests

parameter = {
    "amount":10,
    "type":"boolean"
}
response = requests.get(url="https://opentdb.com/api.php",params=parameter)
data = response.json()
question_data = data["results"]
