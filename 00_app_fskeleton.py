from flask import Flask

# WSGI Application - Tries to communicate b/w app and server
app = Flask(__name__)

'''
Specify a decorator defined with @ symbol, this decorator comes with a binding function 
which will be called automatically as soon as it routes to the path specified in route()

@app.route('/') specifies the url

def welcome():
    return "Welcome to the first flask application, pls subscribe the channel, bhu"
This will be displayed as soon as that url is there

Any number of decorators and functions can be written but the function name and the decorator url should be different
'''

@app.route('/')
def welcome():
    return "Welcome to the first flask application, pls subscribe the channel, bhu"

@app.route('/members')
def members():
    return "My name is Nidhi Kejriwal"


if __name__ == "__main__":
    app.run(debug=True)

