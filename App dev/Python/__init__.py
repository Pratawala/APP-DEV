#This is the main file, connect other files  to it.
from flask import Flask,render_template
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY']='bd5b0be1a4802f93d8007cae7574cefd'  #Encryption stuff to prevent cookie manipulation XSS blah blah blah


@app.route("/")
def home():
    return "Hello world"
#do  not remove this apprently it crashes the entire server when removed


@app.route("/register")
def register():
    form=RegistrationForm()  #creates a form object from Registraion form
    return render_template("register.html",title="Register",form=form)
    #creates a template called register.html

@app.route('/login.form')
def loginform():
    form=LoginForm()
    return render_template("loginform.html",title="login",form=form)


if __name__=="__main__":
    app.run(debug=True)
#nothing below this will work.