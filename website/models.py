from website import db ,login_manager,app
from datetime import datetime
from flask import Flask
from  flask_sqlalchemy import SQLAlchemy 
from  flask_bcrypt import Bcrypt
from itsdangerous import TimeJSONWebSignatureSerializer as Serializer 
from flask_login import UserMixin


# class Note(db.model):
#     id = db.Column(db.Integer, primary_key=True)
#     data = db.Column(db.String(10000))
#     user_id = db.Column(db.Integer, db.ForeignKey('user id'))
    
    

class User(db.Model): #class will be mapped to a table #model allows data to be stored in db files
    id= db.Column(db.Integer ,primary_key=True) #creating column (this is used by sql)
    username= db.Column(db.String(50),unique=True,nullable=False) #Value is a string , 50 character long, unique and cannot be empty
    email= db.Column(db.String(120),unique=True,nullable=False)
    image_file =db.Column(db.String(20),nullable=False,default='default.jpg')
    password =db.Column(db.String(60),nullable=False)

    def get_reset_token(self,expire_sec=1800):
        s = Serializer(app.config['SECRET_KEY'],expire_sec)
        return s.dump({'user_id':self.id}).decode('utf-8')

@staticmethod #dont expect self, only expect the token method as an arguement as self variable is not used
def verify_reset_token(token):
    s= Serializer(app.config['SECRET_KEY']) #s is a class serializer object
    try:
        user_id=s.loads(token)['user_id'] #check for validity of token
    except:
        return None 
    return User.query.get(user_id) #returns user wit the user id


# def create():
#     pass
# def update():
#     pass

# def read():
#     pass
# def delete():
#     User.query.filter_by(id=id).delete()
#     db.session.commit()

# try:

# confirm_password=db.Column(db.String(60),nullable=False)
# except  password!=confirm_password:

    
    # subscription_type=db.Column(db.String(1),default=1)
    #post=db.relationship('Post',backref="author",lazy=True)

def __repr__(self):#what will be printed when the user is created
    return f"User('{self.username}','{self.email}','{self.image_file}')"

class admin(User.Model):
    pass


class master(User.Model):
    id= db.Column(db.Integer ,primary_key=True)
    pin= db.Column(db.Integer(4),unique=False,nullable=False)
    subscription=db.Column(db.Boolean,nullable=False)

class sub(User.Model):
    id= db.Column(db.Integer ,primary_key=True)
name= db.Column(db.String(50),unique=True,nullable=False)
image_file =db.Column(db.String(20),nullable=False,default='default.jpg')
pin= db.Column(db.Integer(4),unique=False,nullable=False)




# class Post(db.Model): #
#     id=db.Column(db.Integer,primary_Key=True) 
#     title=db.Column(db.String(100),nullable=False)
#     date_posted= db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
#     content= db.Column(db.Text,nullable=False)
#     user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)


# def __repr__(self):#what will be printed when the user is created
#     return f"User('{self.title}','{self.date_posted}')"

