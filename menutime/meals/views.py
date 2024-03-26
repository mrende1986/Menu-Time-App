from flask import render_template,redirect,flash,url_for,abort,request,Blueprint
from menutime.meals.forms import CommentForm
from menutime.models import Meal_Details, Comment
from menutime import db
from functools import wraps
from flask_login import login_required, current_user
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from menutime import app

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
    all_meals = db.session.query(Meal_Details).all()
    return render_template('meals.html', meal_stack=all_meals)

@meal.route("/edit", methods=["GET", "POST"])
# @admin_only
def edit():
    
    if request.method == "POST":
        meal_id = request.form["id"]
        meal_to_update = Meal_Details.query.get(meal_id)
        meal_to_update.meal_name = request.form["name"]
        meal_to_update.recipe_category = request.form["category"]
        meal_to_update.ingredients = request.form["ingredients"]
        meal_to_update.link = request.form["link"]
        meal_to_update.servings = request.form["servings"]
        meal_to_update.image_url = request.form["image_url"]
        db.session.commit()
        return redirect(url_for('core.index'))

    meal_id = request.args.get('id')
    meal_selected = Meal_Details.query.get(meal_id)
    return render_template("edit_meal.html", meal=meal_selected)


@meal.route("/meal/<int:meal_id>", methods=["GET", "POST"])
def show_post(meal_id):
    comment_form = CommentForm()
    requested_meal = db.session.query(Meal_Details).get(meal_id)
    
    if comment_form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for("users.login"))

        new_comment = Comment(
            text=comment_form.comment_text.data,
            user_id=current_user.id,
            meal_id=meal_id
        )
        db.session.add(new_comment)
        db.session.commit()

    return render_template("meal.html", meal=requested_meal, form=comment_form, current_user=current_user)


# CREATE
@meal.route('/create',methods=['GET','POST'])
def create_meal():

    if request.method == "POST":

        # global category_selected, desired_servings
        new_meal = []
        new_meal.append(request.form["name"])
        new_meal.append(request.form["category"])
        new_meal.append(request.form["ingredients"])
        new_meal.append(request.form["description"])
        new_meal.append(request.form["link"])
        new_meal.append(request.form["servings"])
        new_meal.append(request.form["image_url"])

        db.session.add(new_meal)
        db.session.commit()
        flash('New Meal Created')
        return redirect(url_for('core.index'))

    return render_template('create_meal.html')
