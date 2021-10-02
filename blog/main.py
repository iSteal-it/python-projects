from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user, login_manager
from forms import CreatePostForm,RegisterForm,LoginForm,CommentForm
from flask_gravatar import Gravatar

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    post = relationship("BlogPost",backref = 'author')
    comments = relationship('Comments',backref = 'author_comment')


class BlogPost(db.Model):
    __tablename__ = "Blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey('Users.id'))
    comments = relationship('Comments',backref = "comment")


class Comments(db.Model):
    __tablename__ = "Comments"
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50))
    post_id = db.Column(db.Integer)


db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    id = 0
    if current_user.is_authenticated:
        id = current_user.id
    return render_template("index.html", all_posts=posts,logged_in=current_user.is_authenticated,id=id)


@app.route('/register',methods=['POST','GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        usrs = User.query.filter_by(email=email).first()
        if usrs:
            flash("Email Already Exist Please Use Different Email To Register Or Login")
            return redirect(url_for('register'))
        else:
            password = form.password.data
            name = form.name.data

            password_hashed = generate_password_hash(password=password, method="pbkdf2:sha256", salt_length=8)

            usr = User(name=name, email=email, password=password_hashed)
            db.session.add(usr)
            db.session.commit()

            return redirect(url_for('login'))
    return render_template("register.html",form=form,logged_in=current_user.is_authenticated)


@app.route('/login',methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        usr = User.query.filter_by(email=email).first()
        if usr:
            password = form.password.data

            usr = User.query.filter_by(email=email).first()
            if usr:
                if check_password_hash(usr.password, password):
                    login_user(usr)
                    return redirect('/')
                else:
                    flash("Password Wrong")
                    return redirect(url_for('login'))
        else:
            flash("Email Not Found Please Recheck Credentials")
            return redirect(url_for('login'))

    return render_template("login.html",form=form,logged_in=current_user.is_authenticated)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:post_id>",methods=['POST','GET'])
def show_post(post_id):
    post_id = post_id
    requested_post = BlogPost.query.get(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        date = form.body.data
        author = current_user.name

        print(date)
        return redirect(url_for('show_post',post_id=post_id))
    id = 0
    if current_user.is_authenticated:
        id = current_user.id
    return render_template("post.html", post=requested_post,logged_in=current_user.is_authenticated,id=id,form=form)


@app.route("/about")
def about():
    return render_template("about.html",logged_in=current_user.is_authenticated)


@app.route("/contact")
def contact():
    return render_template("contact.html",logged_in=current_user.is_authenticated)


@app.route("/new-post",methods=['POST','GET'])
@login_required
def add_new_post():
    if current_user.id == 1 or current_user.id == 2:

        form = CreatePostForm()
        if form.validate_on_submit():
            new_post = BlogPost(
                title=form.title.data,
                subtitle=form.subtitle.data,
                body=form.body.data,
                img_url=form.img_url.data,
                author=current_user,
                date=date.today().strftime("%B %d, %Y")
            )
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for("get_all_posts"))
        return render_template("make-post.html", form=form,logged_in=current_user.is_authenticated)
    else :
        return redirect('/')


@app.route("/edit-post/<int:post_id>",methods=['POST','GET'])
@login_required
def edit_post(post_id):
    if current_user.id == 1 or current_user.id == 2:

        post = BlogPost.query.get(post_id)
        edit_form = CreatePostForm(
            title=post.title,
            subtitle=post.subtitle,
            img_url=post.img_url,
            author=post.author,
            body=post.body
        )
        if edit_form.validate_on_submit():
            post.title = edit_form.title.data
            post.subtitle = edit_form.subtitle.data
            post.img_url = edit_form.img_url.data

            post.body = edit_form.body.data
            db.session.commit()
            return redirect(url_for("show_post", post_id=post.id))

        return render_template("make-post.html", form=edit_form,logged_in=current_user.is_authenticated)
    else :
        return redirect('/')


@app.route("/delete/<int:post_id>")
@login_required
def delete_post(post_id):
    if current_user.id == 1 or current_user.id == 2:

        post_to_delete = BlogPost.query.get(post_id)
        db.session.delete(post_to_delete)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    else :
        return redirect('/')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)
