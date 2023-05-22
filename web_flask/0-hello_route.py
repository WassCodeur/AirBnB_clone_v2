#!/usr/bin/python3
from flask import Flask
app = Flask('__name__')


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    enter point - hello_hbnb

    parameter: None

    return: hello HBNB!
    """
    return "hello HBNB!"


if __name__ == '__main__':
    """
    check if the program is lauch as main
    """
    app.run(host='0.0.0.0', port=5000)
