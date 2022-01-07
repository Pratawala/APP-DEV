from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #makes warning message go away
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db' #url of database




db= SQLAlchemy(app)

class User(db.Model): #class will be mapped to a table
    id= db.Column(db.Integer ,primary_key=True) #creating column (this is used by sql)

    #Following columns is for storing data we want
    name= db.column(db.String(50))  #Value is a string and 50 character long
    password=db.Column(db.String(50))
    # subscription_type=db.Column(db.String(1),default=1)



