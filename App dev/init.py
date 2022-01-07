#This is the main file, connect other files  to it.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

@app.route('/')
def home():
    return ("Hello world")

@app.route('/loginform')
def loginform():
    return ('loginform.html')





if __name__=="__main__":
    app.run(debug=True)
#nothing below this will work.