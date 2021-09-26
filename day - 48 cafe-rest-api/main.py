from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def random_cafe():
    cafes = Cafe.query.all()
    cafe = random.choice(cafes)
    js = jsonify(id=cafe.id,name=cafe.name,map_url=cafe.map_url,img_url=cafe.img_url,location=cafe.location,has_sockets=cafe.has_sockets,has_toilet=cafe.has_toilet,has_wifi=cafe.has_wifi,can_take_calls=cafe.can_take_calls,seats=cafe.seats,coffee_price=cafe.coffee_price)
    print(js)
    return js


@app.route("/all")
def get_all():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])

@app.route("/search")
def find_loc():
    query = request.args.get('loc')
    cafes = Cafe.query.filter_by(location=query).all()
    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    else:
        print(0)
    return "Not Found"

@app.route("/add",methods=["POST"])
def add_row():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("has_sockets")),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update-price/<cafe_id>",methods=["PATCH"])
def pch(cafe_id):
    cafe = Cafe.query.filter_by(id=cafe_id).first()
    cafe.coffee_price = request.form.get("price")
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/del/<cafe_id>",methods=["DELETE"])
def p(cafe_id):
    if request.form.get("api") == "xyz":
        cafe = Cafe.query.filter_by(id=cafe_id).first()
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."})
    else:
        return jsonify(response={"success": "Successfully deleted the new cafe."})


if __name__ == '__main__':
    app.run(debug=True)

