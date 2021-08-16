import os

import flask

from app import app


@app.route("/asset/img/<image>")
def get_image(image):
    if image not in os.listdir("falconca/asset/img"):
        flask.abort(404)
    else:
        return flask.send_file(f"falconca/asset/img/{image}")