from flask import render_template, url_for, redirect, request, Blueprint
from flask_login import login_required, current_user
from menutime import db
from menutime.generator.engine import meal_selector, populate_shopping_list
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter
import os

generator = Blueprint('generator',__name__)

@generator.route("/selections", methods=["GET", "POST"])
@login_required
def selections():
    if request.method == "POST":
        global category_selected, desired_servings
        category_selected = []
        category_selected.append(int(request.form["fish_meals"]))
        category_selected.append(int(request.form["chicken_meals"]))
        category_selected.append(int(request.form["beef_meals"]))
        category_selected.append(int(request.form["salad_meals"]))
        category_selected.append(int(request.form["taco_meals"]))
        category_selected.append(int(request.form["vegetarian_meals"]))
        desired_servings = int(request.form["servings"])
        
        return redirect(url_for('generator.menu'))
    
    return render_template('selections.html')

@generator.route('/menu')
@login_required
def menu():
    global category_selected, desired_servings

    try:
        user_id = current_user.id
        this_weeks_ids = meal_selector(category_selected, desired_servings, user_id)
        shopping_list, menu_names, menu_link, menu_image_url, menu_description = populate_shopping_list(this_weeks_ids, desired_servings)
        meals_dict = {
            'id' : this_weeks_ids,
            'names' : menu_names,
            'links' : menu_link,
            'image_url' : menu_image_url,
            'description' : menu_description
        }
        category_selected = []
        desired_servings = []
        return render_template('menu.html', meals=meals_dict, shopping_list=shopping_list)
    
    except (NameError, IndexError):
        try: 

            find_user = db.collection("selections").where(filter=FieldFilter('user_id', '==', user_id)).order_by("created_date", direction=firestore.Query.DESCENDING).limit(1)
            find_user = [doc.to_dict() for doc in find_user.stream()]
            this_weeks_ids_2 = find_user[0]['meal_ids_returned']
            desired_servings_2 = find_user[0]['meal_portions']
            shopping_list, menu_names, menu_link, menu_image_url, menu_description = populate_shopping_list(this_weeks_ids_2, desired_servings_2)
        
            meals_dict = {
                'id' : this_weeks_ids_2,
                'names' : menu_names,
                'links' : menu_link,
                'image_url' : menu_image_url,
                'description' : menu_description
            }
            
            return render_template('menu.html', meals=meals_dict, shopping_list=shopping_list)

        except AttributeError:
            return redirect(url_for('generator.selections'))


@generator.route('/standard')
def standard():

    standard_user_id = os.environ.get("USER_1", None)
    find_user = db.collection("selections").where(filter=FieldFilter('user_id', '==', standard_user_id)).order_by("created_date", direction=firestore.Query.DESCENDING).limit(1)
    find_user = [doc.to_dict() for doc in find_user.stream()]
    standard_ids = find_user[0]['meal_ids_returned']
    standard_servings = find_user[0]['meal_portions']
    shopping_list, menu_names, menu_link, menu_image_url, menu_description = populate_shopping_list(standard_ids, standard_servings)
    
    meals_dict = {
        'id' : standard_ids,
        'names' : menu_names,
        'links' : menu_link,
        'image_url' : menu_image_url,
        'description' : menu_description
    }

    return render_template('standard.html', meals=meals_dict, shopping_list=shopping_list)