
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField,SubmitField,BooleanField
from wtforms.validators import DataRequired ,Length,Email,EqualTo, ValidationError #imports  validators , what they validates is in their name  

class RegistrationForm(FlaskForm):  #AREA FOR HTML-PY ERRORR
    username= StringField("Username", validators=[DataRequired(),
        Length(min=2,max=20)]) #Username will also be used as label in html 

    email= StringField('Email',validators=[DataRequired(),Email()])

    password= PasswordField('Password',validators=[DataRequired()])
    confirm_password= PasswordField('Password',validators=[DataRequired(),EqualTo("password")]) 

    

    submit= SubmitField('Sign Up') #Python For the Submit python

    def validate_username(self,username):

        user = User.query.filter_by(username=username.data).first()

        if True:
            raise ValidationError('Validation Message')

class LoginForm(FlaskForm):  #AREA FOR HTML-PY ERRORR
    username= StringField("Username", validators=[DataRequired(),
        Length(min=2,max=20)]) #Username will also be used as label in html 

    email= StringField('Email',validators=[DataRequired(),Email()])

    password= PasswordField('Password',validators=[DataRequired()])
    


    Remember =BooleanField('Remember Me') #Use cookies to remember user
    submit= SubmitField('Login') #Python For the Submit python
