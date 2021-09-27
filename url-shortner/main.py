from flask import Flask,render_template, redirect, url_for , request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
import random

ext_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def create_ext():
    ext = ""
    for _ in range(5):
        random_letter = random.choice(ext_list)
        ext = ext + random_letter
    return ext


class Urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ext = db.Column(db.String(250), unique=True, nullable=False)
    target = db.Column(db.String(250), nullable=False)

# db.create_all()


class Short(FlaskForm):
    target_url = StringField("Enter Url To Short", validators=[DataRequired(), URL()])
    submit = SubmitField("Submit Post")

@app.route('/',methods=['GET','POST'])
def home():
    if request.args.get("ext"):
        all_urls = db.session.query(Urls).all()
        match_url = ""
        for url in all_urls:
            if url.ext == request.args.get('ext'):
                match_url = url
        if match_url:
            return redirect(f"{match_url.target}")
        else:
            form = Short()
            if form.validate_on_submit():
                all_urls = db.session.query(Urls).all()
                new_ext = create_ext()
                for url in all_urls:
                    if url.ext == new_ext:
                        new_ext = create_ext()
                target = form.target_url.data
                url = Urls(ext=new_ext, target=target)
                db.session.add(url)
                db.session.commit()
                u = f"http://127.0.0.1:5000/?ext={new_ext}"
                return render_template("index.html",u=u)
            return render_template("index.html", form=form)

    else:
        form = Short()
        if form.validate_on_submit():
            all_urls = db.session.query(Urls).all()
            new_ext = create_ext()
            for url in all_urls:
                if url.ext == new_ext:
                    new_ext=create_ext()
            target = form.target_url.data
            url = Urls(ext=new_ext,target=target)
            db.session.add(url)
            db.session.commit()
            u = f"http://127.0.0.1:5000/?ext={new_ext}"
            return render_template("index.html",u = u)
        return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)