
from flask_wtf import FlaskForm
from wtforms import  BooleanField, StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired ,Length,Email,EqualTo, ValidationError #imports  validators , what they validates is in their name  
from website.models import User
from flask_login import current_user
from flask_wtf.file import FIeldl,FIle 


#validates the input fields
class RegistrationForm(FlaskForm):  #AREA FOR HTML-PY ERRORR
    username= StringField("Username", validators=[DataRequired(),
        Length(min=2,max=20)]) #Username will also be used as label in html 

    email= StringField('Email',validators=[DataRequired(),Email()])

    password= PasswordField('Password',validators=[DataRequired()])
    confirm_password= PasswordField('Password',validators=[DataRequired(),EqualTo("password")]) 

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
    


    Remember =BooleanField('Remember Me') #Use cookies to remember user
    submit= SubmitField('Login') #Python For the Submit python



class UpdateaccForm(FlaskForm):  #AREA FOR HTML-PY ERRORR
    username= StringField("Username", validators=[DataRequired(),
        Length(min=2,max=20)]) #Username will also be used as label in html 

    email= StringField('Email',validators=[DataRequired(),Email()])
    #insert code to update profile pic, will add in future
    submit= SubmitField('Save Changes') #Python For the Submit python

    def validate_username(self, username):
        if username.data !=current_user.username:
            user = User.query.filter_by(username=username.data).first()   #Checks if user is already in database
        if user: #if user is True this conditional will be activated
            raise ValidationError('Username is already taken!')
 
    def validate_email(self, email): 
        if email.data !=current_user.username:
            user = User.query.filter_by(email=email.data).first()   #Checks if user is already in database
        if user: #if user is none this conditional will be activated
            raise ValidationError('Email is already in use!')



    class request_reset(FlaskForm):
        email=email= StringField('Email',validators=[DataRequired(),Email()])
        submit =SubmitField('Request Password reset')


        def validate_email(self, email): 
            if email.data !=current_user.username:
                user = User.query.filter_by(email=email.data).first()   #Checks if user is already in database
            if user is None: #if user is none this conditional will be activated
                raise ValidationError('Email is not registered with website')

    
    
    class reset_password(FlaskForm):
         password= PasswordField('Password',validators=[DataRequired()])
    confirm_password= PasswordField('Password',validators=[DataRequired(),EqualTo("password")]) 

    submit= SubmitField("Reset Password")
