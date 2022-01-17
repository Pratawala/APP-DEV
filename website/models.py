from website import db
from datetime import datetime
from flask import Flask
from  flask_sqlalchemy import SQLAlchemy 
from  flask_bcrypt import Bcrypt








# class Note(db.model):
#     id = db.Column(db.Integer, primary_key=True)
#     data = db.Column(db.String(10000))
#     user_id = db.Column(db.Integer, db.ForeignKey('user id'))
    
    


class User(db.Model): #class will be mapped to a table
    id= db.Column(db.Integer ,primary_key=True) #creating column (this is used by sql)
    username= db.Column(db.String(50),unique=True,nullable=False) #Value is a string , 50 character long, unique and cannot be empty
    email= db.Column(db.String(120),unique=True,nullable=False)
    image_file =db.Column(db.String(20),nullable=False,default='default.jpg')
    password =db.Column(db.String(60),nullable=False)
# try:
    
    # confirm_password=db.Column(db.String(60),nullable=False)
# except  password!=confirm_password:

       
        # subscription_type=db.Column(db.String(1),default=1)
        #post=db.relationship('Post',backref="author",lazy=True)

    def __repr__(self):#what will be printed when the user is created
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class admin(User):
    pass
    

class master(User):
     id= db.Column(db.Integer ,primary_key=True)
     pin= db.Column(db.String(4),unique=False,nullable=False)
     subscription=db.Column(db.Boolean,nullable=False)

class servant(User):
    id= db.Column(db.Integer ,primary_key=True)
    username= db.Column(db.String(50),unique=True,nullable=False)
    image_file =db.Column(db.String(20),nullable=False,default='default.jpg')
    pin= db.Column(db.String(4),unique=False,nullable=False)

    


# class Post(db.Model): #
#     id=db.Column(db.Integer,primary_Key=True) 
#     title=db.Column(db.String(100),nullable=False)
#     date_posted= db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
#     content= db.Column(db.Text,nullable=False)
#     user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)


    # def __repr__(self):#what will be printed when the user is created
    #     return f"User('{self.title}','{self.date_posted}')"

