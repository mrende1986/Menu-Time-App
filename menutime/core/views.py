from flask import render_template,Blueprint
from menutime import db
from menutime.my_classes import Query
# from google.cloud.firestore_v1 import aggregation
# from google.cloud.firestore_v1.base_query import FieldFilter
import base64


core = Blueprint('core',__name__)

@core.route('/')
def index():

    return render_template('index.html')


@core.route('/customdetails')
def customdetails():

    return render_template('customdetails.html')


@core.route('/about')
def about():
    query = Query()
    count_of_menus = query.query_num_menus()
    count_of_meals = query.query_num_meals()
    create_chart = query.run_query_and_plot()
    meals_available_image = base64.b64encode(create_chart.getvalue()).decode('utf-8')
    most_pop_meals = query.generate_top_meal_ids_chart()
    most_pop_meals_image = base64.b64encode(most_pop_meals.getvalue()).decode('utf-8')
    types_selected = query.generate_type_selections_chart()
    types_selected_image = base64.b64encode(types_selected.getvalue()).decode('utf-8')

    return render_template('about.html', num_menus=count_of_menus, num_meals=count_of_meals, 
                           meals_available=meals_available_image, most_pop_img = most_pop_meals_image, 
                           types_img = types_selected_image)
