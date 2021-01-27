from os import getenv, urandom
from flask import Flask
from flask_sqlalchemy import sqlalchemy
from dotenv import load_dotenv
# ------------------------------------ #
from flask_auth import app
from flask_auth.database.models import db

load_dotenv()

db.init_app(app) 
db.app = app

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] =  getenv("DATABASE_URL")
app.secret_key = urandom(32)