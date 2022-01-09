from flask import render_template,flash,redirect,url_for,flash,redirect
from website.models import User
from website.forms import RegistrationForm,LoginForm
from website import app

@app.route("/")
def home():
    return render_template("null2.html")
#do  not remove this apprently it crashes the entire server when removed


@app.route("/")
def test():
    return render_template("null2.html")

@app.route("/register",methods=['GET','POST'])
def register():
    form=RegistrationForm()  #creates a form object from Registraion form
    if form.validate_on_submit():
        flash(f'Account successfully created for {form.username.data}!') #flash displays a popup message
        return redirect(url_for("home"))
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