#This is the main file, connect other files  to it.

from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return ("Hello world")




if __name__=="__main__":
    app.run(debug=True)
#nothing below this will work.