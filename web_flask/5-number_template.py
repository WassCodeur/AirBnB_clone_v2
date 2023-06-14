#!/usr/bin/python3
"""
import flask framework to web tools
"""

from flask import Flask, render_template
app = Flask('__name__')


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Entry point - hello_hbnb

    parameter : non

    return : hello HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Entry point - hbnb

    parameter: none

    return: HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Entry point - c_text

    parameter: none

    return: C text
    """
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    Entry point - python_text

    parameter: text

    return: Python text
    """
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """
    Entry point - is_number

    parameter: n

    return: n is a number
    """
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_template(n):
    """
    Entry point - html_template

    parameter n

    return: 5-number.html, n
    """
    return render_template('5-number.html', n=n)
    

if __name__ == '__main__':
    """
    check if my program is the main program
    """
    app.run(host='0.0.0.0', port=5000)
