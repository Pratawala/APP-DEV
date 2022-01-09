from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app= Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #makes warning message go away
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db' #url of database
app.config['SECRET_KEY']='bd5b0be1a4802f93d8007cae7574cefd'  #Encryption stuff to prevent cookie manipulation XSS blah blah blah
db=SQLAlchemy(app)

from website import routes

