from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField,PasswordField
from wtforms import validators, ValidationError



app = Flask(__name__)
app.secret_key = 'kimkeyverykey'

class LoginForm(FlaskForm):
    user_name = TextField("UserName", [validators.Required("Please enter your usernamename.")])
    password = PasswordField("Password",[validators.Required("Please enter your password.")])
    submit = SubmitField("Submit")

@app.route("/",methods = ['GET','POST'])
def home():
    return render_template('index.html')


@app.route("/login",methods = ['GET','POST'])
def get_login():
    formm = LoginForm()
    if formm.validate_on_submit():
        print(formm.user_name.data)
    return render_template('login.html', form=formm)




if __name__ == '__main__':
    app.run(debug=True)