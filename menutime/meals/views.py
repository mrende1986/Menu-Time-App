from flask import render_template,redirect,flash,url_for,abort,request,Blueprint
from menutime.meals.forms import CommentForm
from menutime.models import Meal_Details, Comment
from menutime.generator.engine import populate_shopping_list
from menutime import db
from functools import wraps
from flask_login import login_required, current_user
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from menutime import app
from google.cloud.firestore_v1.base_query import FieldFilter

meal = Blueprint('meal',__name__)
bootstrap = Bootstrap(app)
ckeditor = CKEditor(app)

def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        #If id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        #Otherwise continue with the route function
        return f(*args, **kwargs)        
    return decorated_function



@meal.route('/meals')
def meals():
    ## Firebase ##
    meals = db.collection('meals') 
    all_meals = [doc.to_dict() for doc in meals.stream()]
    return render_template('meals.html', meal_stack=all_meals)


# # Removed 5/28/24
@meal.route("/meal/<int:meal_id>", methods=["GET", "POST"])
def show_post(meal_id):
    # comment_form = CommentForm()
    meal_query = db.collection("meals").where(filter=FieldFilter('id', '==', meal_id))
    requested_meal = [meal.to_dict() for meal in meal_query.stream()]
    requested_meal = requested_meal[0]
    id = [meal_id]

    shopping_list, menu_names, menu_link, menu_image_url, menu_description = populate_shopping_list(id, requested_meal['servings'])
    # if comment_form.validate_on_submit():
    #     if not current_user.is_authenticated:
    #         flash("You need to login or register to comment.")
    #         return redirect(url_for("users.login"))

    #     new_comment = Comment(
    #         text=comment_form.comment_text.data,
    #         user_id=current_user.id,
    #         meal_id=meal_id
    #     )
    #     db.session.add(new_comment)
    #     db.session.commit()

    return render_template("meal.html", meal=requested_meal, shopping_list=shopping_list)#, form=comment_form, current_user=current_user)
