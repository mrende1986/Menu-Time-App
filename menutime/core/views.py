from flask import render_template,Blueprint
from menutime import db
from google.cloud.firestore_v1 import aggregation
from google.cloud.firestore_v1.base_query import FieldFilter


core = Blueprint('core',__name__)

@core.route('/')
def index():

    return render_template('index.html')


@core.route('/customdetails')
def customdetails():

    return render_template('customdetails.html')


@core.route('/about')
def about():
    ## Query number of meals in DB
    collection_ref = db.collection("meals")
    query = collection_ref.where(filter=FieldFilter("name", "!=", ""))
    aggregate_query = aggregation.AggregationQuery(query)
    aggregate_query.count(alias="all")

    results = aggregate_query.get()
    for result in results:
        count_of_meals = result[0].value

    ## Query number of menus in DB
    collection_ref = db.collection("selections")
    query = collection_ref.where(filter=FieldFilter("created_date", "!=", ""))
    aggregate_query = aggregation.AggregationQuery(query)
    aggregate_query.count(alias="all")

    menu_results = aggregate_query.get()
    for result in menu_results:
        count_of_menus = result[0].value

    return render_template('about.html', num_meals = count_of_meals, num_menus = count_of_menus)