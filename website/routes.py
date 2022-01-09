from flask import render_template,flash,redirect,url_for,flash,redirect
from wtforms.validators import Email
from website.models import User
from website.forms import RegistrationForm,LoginForm
from website import app,db,bcrypt


@app.route("/")
def home():
    return render_template("null2.html")
#do  not remove this apprently it crashes the entire server when removed


@app.route("/register",methods=['GET','POST'])
def register():
    form=RegistrationForm()  #creates a form object from Registraion form
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password).decode('utf-8') #hash value will be in string instead of bytes
        user=User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are not able to log in','success')
        flash(f'Account successfully created for {form.username.data}!') #flash displays a popup message
        return redirect(url_for("login"))
    return render_template("register.html",title="Register",form=form)
    #register.html is the file name for the register form

@app.route('/html/loginform',methods=['GET','POST'])
def loginform():
    form=LoginForm
    if form.validate_on_submit():
        if form.email.data=='admin@blog.com' and form.password.data=='kingisme':
            flash('You have been logged in!','sucess')
            return redirect(url_for('home'))
        else:
            flash('Login Unsucessful. Please check username and password','danger')
    return render_template("loginform.html",title="login",form=form)