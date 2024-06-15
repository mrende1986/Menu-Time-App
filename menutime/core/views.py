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
    chart_image = base64.b64encode(create_chart.getvalue()).decode('utf-8')

    return render_template('about.html', num_menus=count_of_menus, num_meals=count_of_meals, image=chart_image)
