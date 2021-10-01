from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

# db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html",logged_in=current_user.is_authenticated)


@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == "POST":
        name= request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        print(password)
        password_hashed = generate_password_hash(password=password,method="pbkdf2:sha256",salt_length=8)
        print(password_hashed)
        usr = User(name=name,email=email,password=password_hashed)
        db.session.add(usr)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("register.html",logged_in=current_user.is_authenticated)


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        usr = User.query.filter_by(email=email).first()
        if usr:
            if check_password_hash(usr.password,password):
                login_user(usr)
                return redirect('secrets')
            else:
                flash("password wrong")
                return redirect(url_for('login'))
        else:
            return "not found"

    return render_template("login.html",logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html",name=current_user.name,logged_in=True)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
def download():
    return send_from_directory('static', filename="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
