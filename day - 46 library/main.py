from flask import Flask, render_template, redirect, url_for,request
from flask_wtf import FlaskForm
from wtforms import StringField
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "vsvnvfvfjvfvjv"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(50))
    rating = db.Column(db.String(200))


db.create_all()


def add_book(title, author, rating):
    book_entry = {
        "title": f"{title}",
        "author": f"{author}",
        "rating": f"{rating}"
    }

    return book_entry


class Book_Form(FlaskForm):
    book = StringField("Book Name")
    author = StringField("Author Name")
    rating = StringField("Rating")


class Edit(FlaskForm):
    rating = StringField("Rating")


@app.route('/')
def home():
    all_books = db.session.query(Books).all()
    print(all_books)
    if len(all_books) == 0:
        return render_template("index.html", a=True)
    return render_template("index.html", a=False, books=all_books)

@app.route('/delete')
def delete_book():
    book_id = request.args.get('id')
    book_selected = Books.query.get(book_id)
    db.session.delete(book_selected)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add():
    form = Book_Form()
    if form.validate_on_submit():
        book = form.book.data
        author = form.author.data
        rating = form.rating.data
        bookadd = Books(title=book, author=author, rating=rating)
        db.session.add(bookadd)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=form)


@app.route('/edit',methods=["GET", "POST"])
def edit_rating():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = Books.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Books.query.get(book_id)
    db.session.delete(book_selected)
    return render_template("", book=book_selected)

if __name__ == "__main__":
    app.run(debug=True)
