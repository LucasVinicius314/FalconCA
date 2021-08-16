import flask

from app import app


@app.route("/")
def home():
    print(f"Real IP: {flask.request.headers.get('X-Real-IP')}")
    return flask.send_file("falconca/root/home.html")