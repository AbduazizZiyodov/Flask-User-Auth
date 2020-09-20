## Setup
Clone repository and change directory:

    $ git clone https://github.com/AbduazizZiyodov/Flask-User-Authentication.git
    $ cd Flask-User-Authentication
Change db configs from file `__init__.py:`

    app.config['SECRET_KEY'] =  '< YOUR SECRET KEY>'
    app.config['SQLALCHEMY_DATABASE_URI'] =  '<DB URI>'
Install packages from requirements.txt:

    $ pip3 install -r requirements.txt
Run server:

    $ python3 server.py
Enjoy ))
