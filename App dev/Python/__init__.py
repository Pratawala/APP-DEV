#This is the main file, connect other files  to it.
from flask import Flask,render_template
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY']='bd5b0be1a4802f93d8007cae7574cefd'  #Encryption stuff to prevent cookie manipulation XSS blah blah blah



@app.route('/')
def loginform():
    return render_template("loginform.html")






if __name__=="__main__":
    app.run(debug=True)
#nothing below this will work.