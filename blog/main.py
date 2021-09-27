from flask import Flask, render_template, redirect, url_for,request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CKEDITOR_PKG_TYPE'] = 'full'
db = SQLAlchemy(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)



class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField('Blog Content',validators=[DataRequired()])
    submit = SubmitField("Submit Post")




@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<id_i>")
def show_post(id_i):
    found_post = BlogPost.query.get(id_i)

    return render_template("post.html", post=found_post)

#  {{url_for('edit_post', post_id=post.id)}}
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/del/<id_i>",methods=["DELETE",'GET'])
def delete_post(id_i):
    found_post = BlogPost.query.get(id_i)
    db.session.delete(found_post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/make-post", methods=['POST','GET'])
def make_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        title = form.title.data
        subtitle = form.subtitle.data
        author = form.author.data
        img_url = form.img_url.data
        body = form.body.data
        dt = datetime.now()
        yr = dt.year
        dy = dt.day
        mt = dt.strftime("%b")
        date = f"{mt} {dy} {yr}"
        post = BlogPost(title=title,subtitle=subtitle,date=date,body=body,author=author,img_url=img_url)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html",form=form)

@app.route("/edit-post/<id_i>", methods=['POST','GET'])
def edit_post(id_i):
    post = BlogPost.query.get(id_i)
    form = CreatePostForm()
    if request.method == 'GET':
        form.title.data = post.title
        form.subtitle.data = post.subtitle
        form.author.data = post.author
        form.body.data = post.body
        form.img_url.data = post.img_url
    if request.method == 'POST':
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.author = form.author.data
        post.img_url = form.img_url.data
        post.body = form.body.data
        dt = datetime.now()
        yr = dt.year
        dy = dt.day
        mt = dt.strftime("%b")
        post.date = f"{mt} {dy} {yr}"
        db.session.commit()
        return redirect(url_for('get_all_posts'))

    return render_template("make-post.html", form=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)