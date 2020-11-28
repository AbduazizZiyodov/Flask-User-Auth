from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy


db= SQLAlchemy()


#User model
class User(db.Model,UserMixin ):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def auth(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"User('{self.email}')"

