from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired
import requests

API_KEY = "9ca05fa7a628d06a0a63e9cd8c022989"
END_POINT = f"https://api.themoviedb.org/3/search/movie"

app = Flask(__name__)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Bootstrap(app)


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    year = db.Column(db.String(50))
    description = db.Column(db.String(200))
    rating = db.Column(db.Float)
    ranking = db.Column(db.String(200))
    review = db.Column(db.String(200))
    img_url = db.Column(db.String(200))


db.create_all()


class Edit(FlaskForm):
    rating = StringField("Rating eg between 0 and 10", validators=[DataRequired()])
    review = StringField("Review")
    submit_button = SubmitField('Submit Form')
    myhidden = HiddenField()


class Add_movie(FlaskForm):
    movie_title = StringField("Movie Title", validators=[DataRequired()])
    submit_button = SubmitField('Submit Form')


@app.route("/")
def home():
    movie_data = Movies.query.order_by(Movies.rating).all()
    for i in range(len(movie_data)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        movie_data[i].ranking = len(movie_data) - i
    db.session.commit()
    return render_template("index.html", movie_data=movie_data)


@app.route("/edit", methods=('GET', 'POST'))
def edit_rating():
    form = Edit(myhidden=request.args.get('id'))
    if form.validate_on_submit():
        rating = form.rating.data
        review = form.review.data
        myhidden = form.myhidden.data
        move_to_update = Movies.query.get(myhidden)
        move_to_update.rating = rating
        move_to_update.review = review
        db.session.commit()
        return redirect(url_for('home'))

    movie_id = request.args.get('id')
    movie_selected = Movies.query.get(movie_id)
    return render_template("edit.html", movie_data=movie_selected, form=form)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get('id')
    movie_selected = Movies.query.get(movie_id)
    db.session.delete(movie_selected)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=('GET', 'POST'))
def add_movie():
    form = Add_movie()
    if form.validate_on_submit():
        title = form.movie_title.data
        response = requests.get(url=END_POINT, params={"api_key": API_KEY, "query": title})
        data = response.json()
        data = data['results']
        return render_template("select.html", data=data)
    return render_template("add.html", form=form)


@app.route("/add/d", methods=('GET', 'POST'))
def add_movie_data():
    movie_id = request.args.get('id')
    response = requests.get(url=f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}")
    data = response.json()
    title = data['original_title']
    description = data['overview']
    year = data['release_date']
    img_url =f"https://image.tmdb.org/t/p/w500{data['poster_path']}"

    new_movie = Movies( title=title, year=year, description=description,img_url=img_url)
    db.session.add(new_movie)
    db.session.commit()


    return redirect(url_for('editt',title=title))


@app.route("/editt", methods=('GET', 'POST'))
def editt():
    movie_title = request.args.get('title')
    form = Edit(myhidden=movie_title)
    movie_selected = Movies.query.filter_by(title=movie_title).first()
    if form.validate_on_submit():
        rating = form.rating.data
        review = form.review.data
        myhidden = form.myhidden.data
        move_to_update = Movies.query.filter_by(title=myhidden).first()
        move_to_update.rating = rating
        move_to_update.review = review
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie_data=movie_selected, form=form)

if __name__ == '__main__':
    app.run(debug=True)
