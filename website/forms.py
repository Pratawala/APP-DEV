
from flask_wtf import FlaskForm
from wtforms import  BooleanField, StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired ,Length,Email,EqualTo, ValidationError #imports  validators , what they validates is in their name  
from website.models import User


#validates the input fields
class RegistrationForm(FlaskForm):  #AREA FOR HTML-PY ERRORR
    username= StringField("Username", validators=[DataRequired(),
        Length(min=2,max=20)]) #Username will also be used as label in html 

    email= StringField('Email',validators=[DataRequired(),Email()])

    password= PasswordField('Password',validators=[DataRequired()])
    confirm_password= PasswordField('Password',validators=[DataRequired(),EqualTo("password")]) 

    submit= SubmitField('Sign Up') #Python For the Submit python

    def validate(self, username): 
        user = User.query.filter_by(username=username.data).first()   #Checks if user is already in database
        if user: #if user is none this conditional will be activated
            raise ValidationError('Username is already taken!')
 
    def validate(self, email): 
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
    


    Remember =BooleanField('Remember Me') #Use cookies to remember user
    submit= SubmitField('Login') #Python For the Submit python
