#!/usr/bin/python3
""" second ex """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def just_hbnb():
    return 'HBNB'

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
