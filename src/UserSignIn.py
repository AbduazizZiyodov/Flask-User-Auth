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
from flask_login import login_user    
from src import app, bcrypt
from src.views import db
from src.database.models import User

"""Login Function"""
def SignIn(request_email, request_password):
        email = request_email
        password = request_password
        user = User.query.filter_by(email = email).first()
        if user and bcrypt.check_password_hash(user.password , password):
            login_user(user)
            return redirect(url_for('content'))
        else:
            flash("Email or password is incorrect!" , 'danger')

