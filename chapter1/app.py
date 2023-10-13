'''
In this i am going to use pip to import the 3 party module 
pip is package manager used by python for importing of external library

ex_1 -> pip install Flask
ex_2 -> pip install tenserflow

if you want to install leatest version 
ex_3 -> pip install -U Flask 
'''

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hellow App"

@app.route("/about")
def aboud():
    return "Hello about"

'''
in order to run this app use command
flask run
'''