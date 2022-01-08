from flask import Flask

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return 'hello, world!'


app.debug = True
app.run() 
