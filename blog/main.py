from flask import Flask
from flask import render_template
from flask import request
import requests
import smtplib

app = Flask(__name__)

@app.route("/")
def home():
    response = requests.get(url="https://api.npoint.io/5365165e396bedbffeb0")
    data = response.json()
    return render_template("index.html",data=data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact",methods=["POST"])
def get_data():
    name = request.form["name"]
    mail = request.form["email"]
    phone = request.form["phone"]
    txt = request.form["text"]
    my_email = "rus@pixelpaste.net"
    password = "Krevory123@"
    connection = smtplib.SMTP("smtp.hostinger.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="bobbobpvp@gmail.com",
        msg=f"From:Admin@pixelpaste.net\nSubject:Blog Form\n\n {name}\n{mail}\n{phone}\n{txt}"
    )
    connection.close()
    return "got it"

@app.route("/b/<title>")
def post(title):
    print(title)
    response = requests.get(url="https://api.npoint.io/5365165e396bedbffeb0")
    data = response.json()
    for _ in data:
        if _["title"] == title:
            return render_template("post.html",data=_)

if __name__ == "__main__":
    app.run(debug=True)