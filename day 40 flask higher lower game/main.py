from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0,9)

@app.route("/")
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1> " \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<int:num>")
def ans(num):
    if num > random_number:
        return f"<h1>Higher</h1>" \
           f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif num < random_number:
        return f"<h1>Lower</h1>" \
               f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return f"<h1>correct</h1>" \
               f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
