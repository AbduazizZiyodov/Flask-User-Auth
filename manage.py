from flask import Flask
from flask_script import Manager
from flask_moment import Moment
from flask_migrate import Migrate, MigrateCommand
# --------------------------------------------- #
from flask_auth import app
from flask_auth.config import db


moment = Moment(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def prepare():
    db.session.commit()
    db.drop_all()
    db.create_all()

@manager.command
def runserver(): 
    app.run()

if __name__ == '__main__':
    manager.run()