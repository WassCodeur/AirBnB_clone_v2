#!/usr/bin/python3
from flask import Flask
app = Flask('__name__')


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Entry - point hello_hbnb

    parameters : None

    return : hello HBNB!
    """
    return "hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Entry - point hbnb

    parameters : None

    return : HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Entry - point : c_text

    paraeters : text(string)

    return : C text
    """
    text = text.replace("_", " ")
    return 'C {}'.format(text)


if __name__ == "__main__":
    """
    check if the program is the main program
    """
    app.run(host='0.0.0.0', port=5000)
