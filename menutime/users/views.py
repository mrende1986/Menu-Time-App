from flask import render_template, url_for, flash, redirect, request, Blueprint, session, abort
import os
import pathlib
import json
from flask_login import login_user, current_user, logout_user, login_required
from oauthlib.oauth2 import WebApplicationClient
import requests

from werkzeug.security import generate_password_hash,check_password_hash
from menutime import db, login_manager
from menutime.models import User, Comment
from menutime.users.forms import RegistrationForm,LoginForm,UpdateUserForm
from menutime.users.picture_handler import add_profile_pic
from menutime.email.email import email_new_registration

from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
import google_auth_oauthlib.flow
import google.auth.transport.requests
from pip._vendor import cachecontrol

users = Blueprint('users',__name__)

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)

# GOOGLE_PROJECT_ID = os.environ.get("GOOGLE_PROJECT_ID", None)
GOOGLE_DISCOVERY_URL = ("https://accounts.google.com/.well-known/openid-configuration")

client = WebApplicationClient(GOOGLE_CLIENT_ID)

# Flask-Login helper to retrieve a user from our db
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# register
@users.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()

        email_new_registration(form.email.data)
        flash('Thanks for registration!')
        login_user(user)
        return redirect(url_for('generator.selections'))

    return render_template('register.html',form=form)

# Login
def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()

@users.route("/login")
def login():
    session.permanent = True
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
        )
    return redirect(request_uri)



@users.route("/login/callback")
def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    result = "<p>code: " + code + "</p>"

    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send a request to get tokens! Yay tokens!
    temp_var_url = request.url
    if "http:" in temp_var_url:
        temp_var_url = "https:" + temp_var_url[5:]
    # temp_var_base_url = request.base_url
    # if "http:" in temp_var_base_url:
    #     temp_var_base_url = "https:" + temp_var_base_url[5:]
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=temp_var_url,
        redirect_url=request.base_url,
        code=code,
    )
    
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

    # Now that you have tokens (yay) let's find and hit the URL
    # from Google that gives you the user's profile information,
    # including their Google profile image and email
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    result = result + "<p>token_response: " + token_response.text + "</p>"

    # return result

    # You want to make sure their email is verified.
    # The user authenticated with Google, authorized your
    # app, and now you've verified their email through Google!
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_name = userinfo_response.json()["given_name"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
    else:
        return "User email not available or not verified by Google.", 400

    # Create a user in your db with the information provided
    # by Google
    user = User(
        id=unique_id, username=users_name, email=users_email, profile_image=picture
)

    # Doesn't exist? Add it to the database.
    if not User.get(user_id=unique_id):
        User.create(id=unique_id, username=users_name, email=users_email, profile_image=picture)

    # Begin user session by logging the user in
    login_user(user)

    # Send user back to homepage
    return redirect(url_for("core.index"))

# logout
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("core.index"))

# Account
@users.route("/account", methods=["GET","POST"])
@login_required
def account():

    form = UpdateUserForm()
    if form.validate_on_submit():

        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.picture.data,username)
            current_user.profile_image = pic

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('User Account Update!')
        return redirect(url_for('users.account'))

    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_image = url_for('static', filename='profile_pics/' + current_user.profile_image)
    return render_template('account.html',profile_image=profile_image,form=form)

@users.route("/<username>")
def user_posts(username):
    page = request.args.get('page',1,type=int)
    user = User.query.filter_by(username=username).first_or_404()
    comments = Comment.query.filter_by(user_id=user.id).order_by(Comment.created_date.desc()).paginate(page=page,per_page=5)
    return render_template('user_comments.html',comments=comments,user=user)
