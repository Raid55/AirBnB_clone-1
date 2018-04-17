#!/usr/bin/python3
""" list from db """

from flask import render_template
from flask import Flask
from models import storage, State, City


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def list_states_and_cities():
    return render_template(
        '8-cities_by_states.html',
        states=storage.all(State),
        cities=storage.all(City)
    )


@app.teardown_appcontext
def tear_down(exceptions):
    storage.close()


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
