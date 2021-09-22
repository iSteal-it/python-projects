from flask import Flask, render_template, redirect,url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired,URL
import csv
from csv import writer


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired(message="Enter Cafe Name")])
    cafe_Loc = StringField('Cafe Location On Google Maps (URL)',validators=[DataRequired(message="Enter Cafe Url"),URL(message="Invalid Url")])
    open_time = StringField('Opening Time eg: 9AM', validators=[DataRequired(message="Enter Opening Time")])
    close_time = StringField('Opening Time eg: 9PM', validators=[DataRequired(message="Enter Opening Time")])
    coffee = SelectField('Coffee Rating',choices=["☕","☕☕","☕☕☕","☕☕☕☕","☕☕☕☕☕"])
    wifi = SelectField('Wifi Strength',choices=["✘","💪","💪💪","💪💪💪","💪💪💪💪","💪💪💪💪💪"])
    plug = SelectField('Power Outlets',choices=["✘","🔌","🔌🔌","🔌🔌🔌","🔌🔌🔌🔌","🔌🔌🔌🔌🔌"])
    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST','GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_name = form.cafe.data
        cafe_url = form.cafe_Loc.data
        opens = form.open_time.data
        close = form.close_time.data
        coffee = form.coffee.data
        wifi = form.coffee.data
        plug = form.plug.data
        fields = [cafe_name,cafe_url, opens,close,coffee,wifi,plug]

        with open('cafe-data.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(fields)
            f_object.close()

        return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        list_of_rows.pop(0)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
