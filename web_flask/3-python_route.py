#!/usr/bin/python3
"""
import flask framework to use web tools
"""

from flask import Flask
app = Flask('__name__')


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Entry point - hello_hbnb

    parameters : none

    return : Hello HBNB
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Entry point - hbnb

    parameter : none

    return : HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Entry point - c_text

    parameter : text

    return : C text
    """
    text = text.replace("_", " ")
    return 'C {}'.format(text)


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Entry piont - python_text

    parameters : text

    return : Python text
    """
    text = text.replace("_", " ")
    return 'Python {}'.format(text)


if __name__ == '__main__':
    """
    check if the program is the main program
    """
    app.run(host='0.0.0.0', port=5000)
