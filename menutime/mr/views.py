from flask import render_template,Blueprint
from menutime import db
from menutime.my_classes import Query
# from google.cloud.firestore_v1 import aggregation
# from google.cloud.firestore_v1.base_query import FieldFilter
import base64


mr = Blueprint('mr',__name__)

@mr.route('/')
def index():

    return render_template('index.html')