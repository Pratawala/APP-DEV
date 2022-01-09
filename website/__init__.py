from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config('SECRET_KEY') = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Note
    
    return app

app= Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #makes warning message go away
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db' #url of database
app.config['SECRET_KEY']='bd5b0be1a4802f93d8007cae7574cefd'  #Encryption stuff to prevent cookie manipulation XSS blah blah blah
db=SQLAlchemy(app)
bcrypt= Bcrypt(app)

from website import routes

