from flask import (
    Flask, 
    render_template, 
    url_for, 
    flash, 
    redirect, 
    request, 
    )
from flask_login import login_user, current_user, logout_user, login_required

from auth import app, db ,bcrypt
from auth.models import User
from auth.register.user_signup import authenticate
from auth.login.user_signin import signin


""" Simple Content)) """
@app.route('/')
def content():
    return render_template('page.html')


""" Register Route """
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


""" Login Route """
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('content'))

    elif request.method == "POST":
        email = request.form["email"]
        password = request.form["passwd"]

        signin(email, password)

        if current_user.is_authenticated:
            return redirect(url_for('content'))

    return render_template('login.html')

""" Logout """
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('content'))

  
