#!/usr/bin/python3
from flask import Flask
app = Flask('__name__')


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Entry point - hello_hbnb

    parameters : None

    return : hello HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Entry point - hbnb

    parameters : None

    return : HBNB
    """
    return "HBNB"


if __name__ == '__main__':
    """
    check if the program is the main program
    """
    app.run(host='0.0.0.0', port=5000)
