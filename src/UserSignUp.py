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
from flask_login import current_user

from src import app ,bcrypt
from src.views import db
from src.database.models import User
from src.UserSignIn import SignIn


""" Register Function """
def authenticate(request_email, request_username, request_passwd ):  
        # Simple Validation
        if User.query.filter_by(email=request_email).first(): 
            flash('This email is already taken' , 'danger')

        elif User.query.filter_by(username=request_username).first(): 
            flash('This username is already taken' , 'danger') 

        elif len(request_passwd) < 8:
            flash("Password must be at least 8 characters!", 'warning')  

        else:
            hashed_password = bcrypt.generate_password_hash(request_passwd).decode('utf-8')
            new_user = User(username=request_username,email=request_email,password=hashed_password)

            try:
                new_user.auth()

            except:
                return jsonify({
                    "Success": False
                })    
    
            SignIn(request_email , request_passwd)

            