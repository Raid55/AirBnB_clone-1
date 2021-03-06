#!/usr/bin/python3
""" list from db """

from flask import render_template
from flask import Flask
from models import storage, State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    return render_template('7-states_list.html', states=storage.all(State))


@app.teardown_appcontext
def tear_down(exceptions):
    storage.close()


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
