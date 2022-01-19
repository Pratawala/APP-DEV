import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail


db = SQLAlchemy()
DB_NAME = "database.db"



app= Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #makes warning message go away
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db' #url of database
app.config['SECRET_KEY']='bd5b0be1a4802f93d8007cae7574cefd'  #Encryption stuff to prevent cookie manipulation XSS blah blah blah
db=SQLAlchemy(app)
bcrypt= Bcrypt(app)
app.config['MAIL_SERVER']='smtp.google.mail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']=os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD']=os.environ.get('EMAIL_PASS')
mail=Mail(app)

from website import routes

