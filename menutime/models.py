from menutime import db,login_manager
import sqlite3
from sqlalchemy.sql import func
from flask_login import UserMixin
from datetime import datetime
from menutime import db

# flask db migrate -m "migration note"
# flask db upgrade

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.BigInteger, unique=True, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    profile_image = db.Column(db.String(20),nullable=False, default='default_profile.png')
    created_date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    
    def __init__(self,id,username,email,profile_image):
        self.id = id
        self.username = username
        self.email = email
        self.profile_image = profile_image

    def __repr__(self):
        return f"Username {self.username}"
        
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    @staticmethod
    def get(user_id):
        
        # POSTGRESQL
        # user = db.engine.execute('SELECT * FROM user WHERE id=(%s);' , (user_id))

        # USE THIS FOR SQLITE
        user = db.engine.execute(
            "SELECT * FROM user WHERE id = ?", (user_id,)
        ).fetchone()

        if not user:
            return None

        user = User(
            id=user[0], username=user[1], email=user[2], profile_image=user[3]
        )
        return user


    @staticmethod
    def create(id, username, email, profile_image):
        # db = db()
        user = User(id=id, username=username, email=email, profile_image=profile_image)
        db.session.add(user)
        db.session.commit()
        # db.engine.execute(
        #     "INSERT INTO user (id, username, email, profile_image)"
        #     " VALUES (?, ?, ?, ?)",
        #     (id, username, email, profile_image),
        # )
        # db.commit()

class Meal_Details(db.Model,UserMixin):
    __tablename__ = "meal_details"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    category = db.Column(db.String(250), nullable=False)
    ingredients = db.Column(db.JSON, nullable=False)
    description = db.Column(db.String(750), nullable=False)
    link = db.Column(db.String(700), nullable=False)
    servings = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(700), nullable=False)
    created_date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    def __init__(self,id,name,category,ingredients,description,link,servings,image_url):
        self.id = id
        self.name = name
        self.category = category
        self.ingredients = ingredients
        self.description = description
        self.link = link
        self.servings = servings
        self.image_url = image_url

    def __repr__(self):
        return f"Meal {self.name} -- Date: {self.created_date}"

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

class Selections(db.Model):
    __tablename__ = "selections"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    meal_selections = db.Column(db.JSON, nullable=False)
    meal_portions = db.Column(db.Integer, nullable=False)
    meal_ids_returned = db.Column(db.JSON, nullable=True)
    created_date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    def __init__(self,user_id,meal_selections,meal_portions,meal_ids_returned):
        self.user_id = user_id
        self.meal_selections = meal_selections
        self.meal_portions = meal_portions
        self.meal_ids_returned = meal_ids_returned

    # def __repr__(self):
    #     return f"Meal {self.name} -- Date: {self.created_date}"

class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    meal_id = db.Column(db.Integer, db.ForeignKey("meal_details.id"))
    created_date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    def __init__(self,text, user_id, meal_id, created_date):
        self.text = text
        self.user_id = user_id
        self.meal_id = meal_id
        self.created_date = created_date

    def __repr__(self):
        return f"Text {self.text} -- Date: {self.created_date}"