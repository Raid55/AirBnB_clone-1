#!/usr/bin/python3
""" fourth ex """

from flask import Flask


app = Flask(__name__)


def rmv_spaces(string):
    return string.replace('_', ' ')


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def just_hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    return 'c {}'.format(rmv_spaces(text))


@app.route('/python', defaults={'text': "is cool"})
@app.route('/python/', defaults={'text': "is cool"})
@app.route('/python/<text>')
def python_is(text):
    return 'Python {}'.format(rmv_spaces(text))


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
