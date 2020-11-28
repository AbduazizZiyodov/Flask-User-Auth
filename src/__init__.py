from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from src.database.models import User


app = Flask(__name__)
app.config['SECRET_KEY'] = '$ecret07/rwefr*fre35y*gdrgdecret24adjmhk'

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

from src import views

