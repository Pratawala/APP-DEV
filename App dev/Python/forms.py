from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields.simple import PasswordField, StringField,SubmitField,remember,BooleanField
from wtforms.validators import DataRequired ,Length,Email,EqualTo #imports  validators , what they validates is in their name  

class RegistrationForm(FlaskForm):  #AREA FOR HTML-PY ERRORR
    username= StringField("Username", validators=[DataRequired(),
        Length(min=2,max=20)]) #Username will also be used as label in html 

    email= StringField('Email',validators=[DataRequired(),Email()])

    password= PasswordField('Password',validators=[DataRequired()])
    confirm_password= PasswordField('Password',validators=[DataRequired(),EqualTo("password")]) 



    submit= SubmitField('Sign Up') #Python For the Submit python


class LoginForm(FlaskForm):  #AREA FOR HTML-PY ERRORR
    username= StringField("Username", validators=[DataRequired(),
        Length(min=2,max=20)]) #Username will also be used as label in html 

    email= StringField('Email',validators=[DataRequired(),Email()])

    password= PasswordField('Password',validators=[DataRequired()])
    


    remember =BooleanField('Remember Me') #Use cookies to remember user
    submit= SubmitField('Login') #Python For the Submit python
