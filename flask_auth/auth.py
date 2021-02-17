from flask import (
    Flask, 
    render_template, 
    url_for, 
    flash, 
    redirect, 
    request, 
    abort,
    jsonify
    )
from functools import wraps    
from flask_login import login_user, current_user    
from flask_auth import app, bcrypt
from flask_auth.config import db
from flask_auth.database.models import User


"""
Login Function
"""
def SignIn(request_email, request_password):
        email = request_email
        password = request_password
        user = User.query.filter_by(email = email).first()
        if user and bcrypt.check_password_hash(user.password , password):
            login_user(user)
            return redirect(url_for('content'))

        flash("Email or password is incorrect!" , 'danger')


""" 
Register Function 
"""

def authenticate(request_email, request_username, request_passwd ):  
        if User.query.filter_by(email=request_email).first(): 
            flash('This email is already taken' , 'danger')

        elif User.query.filter_by(username=request_username).first(): 
            flash('This username is already taken' , 'danger') 

        elif len(request_passwd) < 8:
            flash("Password must be at least 8 characters!", 'warning')  

        else:
            hashed_password = bcrypt.generate_password_hash(request_passwd)\
                                                            .decode('utf-8')
            new_user = User(username=request_username,email=request_email,password=hashed_password)

            try:
                new_user.auth()

            except Exception:
                return jsonify({
                    "Success": False
                })    

            SignIn(request_email , request_passwd)          

def auth_required(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if current_user.is_authenticated == False:
                flash('Avval tizimga kiring', 'danger')
                return redirect(url_for('content', next=request.url))
            return f(*args, **kwargs)
        return wrapper                