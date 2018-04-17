#!/usr/bin/python3
""" sixth ex """

from flask import render_template
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


@app.route('/number/<int:num>')
def is_number(num):
    return '{} is a number'.format(num)


@app.route('/number_template/<int:num>')
def number_template(num):
    return render_template("5-number.html", number=num)


@app.route('/number_odd_or_even/<int:num>')
def number_isOdd_template(num):
    return render_template("6-number_odd_or_even.html", number=num)


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
