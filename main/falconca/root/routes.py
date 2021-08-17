import flask

from app import app


@app.route("/")
def home():
    return flask.send_file("falconca/root/home.html")