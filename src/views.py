from flask import (
    Flask, 
    render_template, 
    url_for, 
    flash, 
    redirect, 
    request, 
    )
from flask_login import login_user, current_user, logout_user, login_required

from src import app
from src.database.models import User, db
from src.UserSignUp import authenticate
from src.UserSignIn import SignIn


db.init_app(app)
db.app = app

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database/db.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.create_all()


""" HomePage """
@app.route('/')
def content():
    return render_template('page.html')



""" Register Controller"""
@app.route('/register' ,methods = ['GET', 'POST'])
def register(): 
    if current_user.is_authenticated:
        return redirect(url_for('content'))

    elif request.method == "POST":
        email, username, password = request.form["email"] , request.form["username"] ,request.form["passwd"]
        
        authenticate(email , username , password)

        if current_user.is_authenticated:
            return redirect(url_for('content'))

    return render_template('register.html')      


""" Login Controller """
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('content'))

    elif request.method == "POST":
        email,password = request.form["email"] , request.form["passwd"]

        SignIn(email, password)

        if current_user.is_authenticated:
            return redirect(url_for('content'))

    return render_template('login.html')


""" Logout """
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('content'))

  
