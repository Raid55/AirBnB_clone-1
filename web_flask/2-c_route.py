#!/usr/bin/python3
""" third ex """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def just_hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    return 'c {}'.format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
