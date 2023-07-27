from flask import render_template,Blueprint

core = Blueprint('core',__name__)

@core.route('/')
def index():

    return render_template('index.html')


@core.route('/customdetails')
def customdetails():

    return render_template('customdetails.html')

@core.route('/about')
def about():

    return render_template('about.html')