from flask import Flask
from flask import render_template
from datetime import date
import requests

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    name = name.title()
    response = requests.get(f"https://api.agify.io/?name={name}")
    data = response.json()

    response = requests.get(f"https://api.genderize.io/?name={name}")
    da = response.json()

    todays_date = date.today()
    return render_template("index.html",date=todays_date.year,name=name,age=data["age"],gender=da["gender"])

if __name__ == "__main__":
    app.run(debug=True)