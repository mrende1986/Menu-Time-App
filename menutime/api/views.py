from flask import render_template,Blueprint,jsonify
from menutime import db
from menutime.models import Meal_Details, Selections, User

api = Blueprint('api',__name__)




@api.route("/all_meals")
def get_all_meals():
    meals = db.session.query(Meal_Details).all()
    return jsonify(meals=[meal.to_dict() for meal in meals])

@api.route("/all_users")
def get_all_users():
    users = db.session.query(User).all()
    return jsonify(users=[user.to_dict() for user in users])