# this file responsible do define this directory as package
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy # sqlite3
# SQLAlchemy - this library is used as an Object Relational Mapper (ORM) 
# tool that translates Python classes to tables on relational databases 
# and automatically converts function calls to SQL statements

app = Flask(__name__) # __name__ referes to local file 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' # db identifier
app.config['SECRET_KEY'] = '0efccdfd7c44f747820390f1'
db = SQLAlchemy(app)

from market import routes
