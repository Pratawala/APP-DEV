
from sqlite3 import Date
from flask_wtf import FlaskForm
from sqlalchemy import false
from wtforms import  BooleanField, StringField, PasswordField,SubmitField,DateTimeField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired ,Length,Email,EqualTo, ValidationError #imports  validators , what they validates is in their name  
from website.models import User
from flask_login import current_user
import re
# from flask_wtf.file import FIeldl,FIle 


#validates the input fields
class RegistrationForm(FlaskForm):  #AREA FOR HTML-PY ERRORR
    username= StringField("Username", validators=[DataRequired(),
        Length(min=2,max=20)])  #Username will also be used as label in html 

    email= StringField('Email',validators=[DataRequired(),Email()])


    
    password= PasswordField('Password',validators=[DataRequired(),
        Length(min=8)])
    confirm_password= PasswordField('Confirm Password',validators=[DataRequired(),EqualTo("password","Passwords does not match!")]) 
   

    submit= SubmitField('Make Payment') #Python For the Submit python

    def validate_username(self, username): 
        user = User.query.filter_by(username=username.data).first()   #Checks if user is already in database
        if user: #if user is none this conditional will be activated
            raise ValidationError('Username is already taken!')
 
    def validate_email(self, email): 
        user = User.query.filter_by(email=email.data).first()   #Checks if user is already in database
        if user: #if user is none this conditional will be activated
            raise ValidationError('Email is already in use!')
    
    
   

    submit= SubmitField('Sign Up') #Python For the Submit python

    def validate_username(self, username): 
        user = User.query.filter_by(username=username.data).first()   #Checks if user is already in database
        if user: #if user is none this conditional will be activated
            raise ValidationError('Username is already taken!')
 
    def validate_email(self, email): 
        user = User.query.filter_by(email=email.data).first()   #Checks if user is already in database
        if user: #if user is none this conditional will be activated
            raise ValidationError('Email is already in use!')
   

class SubuserForm(FlaskForm):  #AREA FOR HTML-PY ERRORR
    name= StringField("Username", validators=[DataRequired(),
        Length(min=2,max=20)]) #Username will also be used as label in html 
pin= PasswordField('Password',validators=[DataRequired()])
confirm_pin= PasswordField('Password',validators=[DataRequired(),EqualTo("password")])
submit= SubmitField('Sign Up') #Python For the Submit python
def validate(self, name): 
    user = User.query.filter_by(name=name.data).first()   #Checks if user is already in database
    if user: #if user is none this conditional will be activated
        raise ValidationError('Username is already taken!')


class LoginForm(FlaskForm):  #AREA FOR HTML-PY ERRORR
    username= StringField("Username", validators=[DataRequired(),
        Length(min=2,max=20)]) #Username will also be used as label in html 

    email= StringField('Email',validators=[DataRequired(),Email()])

    password= PasswordField('Password',validators=[DataRequired()])
    


    remember =BooleanField('Remember Me') #Use cookies to remember user
    submit= SubmitField('Login') #Python For the Submit python


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')
            

class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')
        


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
    email=email= StringField('Email',validators=[DataRequired(),Email()])
    submit =SubmitField('Request Password reset')


    def validate_email(self, email): 
        if email.data !=current_user.username:
            user = User.query.filter_by(email=email.data).first()   #Checks if user is already in database
        if user is None: #if user is none this conditional will be activated
            raise ValidationError('Email is not registered with website')
        




class ResetForm(FlaskForm):
        password= PasswordField('Password',validators=[DataRequired()])
confirm_password= PasswordField('Password',validators=[DataRequired(),EqualTo("password")]) 

submit= SubmitField("Reset Password")


class PaymentForm(FlaskForm):
    submit= SubmitField("Make payment")
    

    

