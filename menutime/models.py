from menutime import db,login_manager
# import sqlite3
# from sqlalchemy.sql import func
from flask_login import UserMixin
from datetime import datetime
from menutime import db

# flask db migrate -m "migration note"
# flask db upgrade

@login_manager.user_loader
def load_user(user_id):
    user = db.users.find_one({"id": user_id})
    if user:
        return User(id=user['id'], username=user['username'], email=user['email'], profile_image=user['profile_image'])
    return None

class User(UserMixin):
    __collection__ = "user"

    def __init__(self, id, username, email, profile_image='default_profile.png', created_date=datetime.utcnow()):
        self.id = id
        self.username = username
        self.email = email
        self.profile_image = profile_image
        self.created_date = created_date

    def __repr__(self):
        return f"Username {self.username}"
        
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "profile_image": self.profile_image,
            "created_date": self.created_date
        }

    @staticmethod
    def get(user_id):
        user = db.users.find_one({"id": user_id})
        if not user:
            return None
        return User(id=user['id'], username=user['username'], email=user['email'], profile_image=user['profile_image'])

    @staticmethod
    def create(id, username, email, profile_image='default_profile.png'):
        user = {
            "id": id,
            "username": username,
            "email": email,
            "profile_image": profile_image,
            "created_date": datetime.utcnow()
        }
        db.users.insert_one(user)

class Meal_Details:
    # collection = db["meal_details"]
    
    def __init__(self, id, name, category, ingredients, description, link, servings, image_url, created_date=datetime.utcnow()):
        self.id = id
        self.name = name
        self.category = category
        self.ingredients = ingredients
        self.description = description
        self.link = link
        self.servings = servings
        self.image_url = image_url
        self.created_date = created_date

    def __repr__(self):
        return f"Meal {self.name} -- Date: {self.created_date}"

    def save(self):
        document = {
            "_id": self.id,
            "name": self.name,
            "category": self.category,
            "ingredients": self.ingredients,
            "description": self.description,
            "link": self.link,
            "servings": self.servings,
            "image_url": self.image_url,
            "created_date": self.created_date
        }
        self.collection.insert_one(document)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "ingredients": self.ingredients,
            "description": self.description,
            "link": self.link,
            "servings": self.servings,
            "image_url": self.image_url,
            "created_date": self.created_date
        }

class Selections:
    # collection = db["selections"]

    def __init__(self, user_id, meal_selections, meal_portions, meal_ids_returned, created_date=datetime.utcnow()):
        self.user_id = user_id
        self.meal_selections = meal_selections
        self.meal_portions = meal_portions
        self.meal_ids_returned = meal_ids_returned
        self.created_date = created_date

    def __repr__(self):
        return f"Selection for user {self.user_id} -- Date: {self.created_date}"

    def save(self):
        document = {
            "user_id": self.user_id,
            "meal_selections": self.meal_selections,
            "meal_portions": self.meal_portions,
            "meal_ids_returned": self.meal_ids_returned,
            "created_date": self.created_date
        }
        self.collection.insert_one(document)

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "meal_selections": self.meal_selections,
            "meal_portions": self.meal_portions,
            "meal_ids_returned": self.meal_ids_returned,
            "created_date": self.created_date
        }

class Comment:
    # collection = db["comments"]

    def __init__(self, text, user_id, meal_id, created_date=datetime.utcnow()):
        self.text = text
        self.user_id = user_id
        self.meal_id = meal_id
        self.created_date = created_date

    def save(self):
        document = {
            "text": self.text,
            "user_id": self.user_id,
            "meal_id": self.meal_id,
            "created_date": self.created_date
        }
        self.collection.insert_one(document)

    def __repr__(self):
        return f"Text {self.text} -- Date: {self.created_date}"