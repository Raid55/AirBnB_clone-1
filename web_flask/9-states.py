#!/usr/bin/python3
""" list from db """

from flask import render_template
from flask import Flask
from models import storage, State, City


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def list_states(state_id=None):
    if state_id is None:
        states = storage.all(State)
        cities = None
    else:
        states = [o for o in storage.all(State) if o.id == state_id]
        if not states:
            states = None
            cities = None
        else:
            cities = [o for o in storage.all(City) if o.state_id == state_id]

    return render_template('9-states.html', states=states, cities=cities)


@app.teardown_appcontext
def tear_down(exceptions):
    storage.close()


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
