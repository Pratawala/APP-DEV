import os
import stripe
from flask import Flask , jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_login import LoginManager


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
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

stripe_keys = {
    "secret_key":os.environ["sk_test_51KT4SyFLyxECVHbXNHXKxESqhvT1lJ3u07HTsO0k7Tg9wcDUKS6M7cak6Dm7mRq15US3kEhjpGulrPSswoT3yR6e00J8ORGGR5"],
    "publishable_key":os.environ["pk_test_51KT4SyFLyxECVHbXt3E43EYTXtACTmO51biKlpfQhuMriYsPK9pFJTndsq5yU7fcetS5pAaBZubWgTFXmqIcJhkX00n2Q2FZcQ"]
}

stripe.api_key = stripe_keys["sk_test_51KT4SyFLyxECVHbXNHXKxESqhvT1lJ3u07HTsO0k7Tg9wcDUKS6M7cak6Dm7mRq15US3kEhjpGulrPSswoT3yR6e00J8ORGGR5"]

from website import routes

