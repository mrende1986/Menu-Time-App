from flask import Flask
import os
from flask_login import LoginManager
from flask_mail import Mail
from datetime import timedelta
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", None)
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=5)


##################################
##### DATABASE SETUP #############
##################################
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# Migrate(app,db)

##################################
###### Firebase SETUP ############
##################################
cred = credentials.Certificate('plan-your-grub-firebase-adminsdk-o3ucn-1d07e93951.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

##################################
##### LOGIN CONFIGS ##############
##################################
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

##################################
####### EMAIL CONFIG #############
##################################
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = "menutimeapp@gmail.com"
app.config['MAIL_PASSWORD'] = os.environ.get("MAIL_PASSWORD")
mail = Mail(app)


##################################
######### BLUEPRINT ##############
##################################
from menutime.core.views import core
from menutime.users.views import users
from menutime.error_pages.handlers import error_pages
from menutime.generator.views import generator
from menutime.meals.views import meal
from menutime.api.views import api
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)
app.register_blueprint(generator)
app.register_blueprint(meal)
app.register_blueprint(api)