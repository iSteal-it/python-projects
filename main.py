import requests
import datetime

APP_ID = "dfb4b666"
API_KEY = "f588d64dff092d7a0bd865296afa48c8"

today = datetime.datetime.now()

header = {
    "x-app-id":APP_ID,
    "x-app-key": API_KEY,
    "Content-Type":"application/json"
}

answer = input("what you did today? ")
parameter = {
 "query":answer
}

post_query_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
response = requests.post(url=post_query_url,headers=header,json=parameter)

what_i_did = response.json()

d = (what_i_did["exercises"])

header = {
    "Authorization": "Bearer krevory123",
    "Content-Type": "application/json"
}

for _ in d:
    data = {
        "date": str(today.date()),
        "time": str(today.strftime("%H:%M:%S")),
        "exercise": _['name'],
        "duration": _['duration_min'],
        "calories": _['nf_calories']

    }
    sen = {"workout": data}
    post_sheety_url = "https://api.sheety.co/b12703464b519b11311d5ecf11464c42/workout/workouts"

    response = requests.post(url=post_sheety_url, headers=header, json=sen)
    print(response.text)
