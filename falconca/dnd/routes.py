import os

import flask

from app import app


@app.route("/dnd")
def index():
    return flask.send_file("falconca/dnd/index.html")


@app.route("/dnd/<file>")
def doc(file):
    if file not in os.listdir("falconca/dnd/docs"):
        flask.abort(404)
    else:
        return flask.send_file(f"falconca/dnd/docs/{file}")