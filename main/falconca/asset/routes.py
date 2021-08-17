import os

import flask

from app import app

CHUNK_SIZE = 4096


@app.route("/asset/img/<image>")
def get_image(image):
    if image not in os.listdir("falconca/asset/img"):
        flask.abort(404)
        return

    def buffer():
        with open(f"falconca/asset/img/{image}", "rb") as file_f:
            while True:
                data = file_f.read(CHUNK_SIZE)
                if not data:
                    break
                yield data

    return flask.Response(flask.stream_with_context(buffer()))


@app.route("/asset/css/<css_file>")
def get_css(css_file):
    if css_file not in os.listdir("falconca/asset/css"):
        flask.abort(404)
        return
    return flask.send_file(f"falconca/asset/css/{css_file}")