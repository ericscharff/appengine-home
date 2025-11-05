import datetime
import secrets

from flask import Flask, make_response, render_template, request

app = Flask(__name__)

BUILD_DATE = 'Last modified Tue Nov  4 06:31:22 PM MST 2025'


@app.route("/calc")
@app.route("/calc/")
@app.route("/calc/index.html")
def calc_main():
    return render_template("calc/index.html")


@app.route("/calc/manifest.json")
def calc_manifest():
    resp = make_response(render_template("calc/manifest.json"))
    resp.mimetype = 'application/json'
    return resp


@app.route("/homeapp")
@app.route("/homeapp/")
@app.route("/homeapp/index.html")
def homeapp_main():
    current_date = (
        datetime.datetime.utcnow() +
        datetime.timedelta(hours=-6)).isoformat()
    return render_template("homeapp/index.html", current_date=current_date)


@app.route("/homeapp/runner")
def homeapp_runner():
    return render_template("homeapp/runner.html")


@app.route("/homeapp/manifest.json")
def homeapp_manifest():
    resp = make_response(render_template("homeapp/manifest.json"))
    resp.mimetype = 'application/json'
    return resp


@app.route("/check_token")
def check_update():
    message = f'Your token was {request.args.get('token', 'nothing')}.'
    return {'message': message, 'next_token': secrets.token_urlsafe(16)}


@app.route("/")
def root():
    current_date = (
        datetime.datetime.utcnow() +
        datetime.timedelta(hours=-6)).isoformat()
    return render_template(
        "index.html",
        build_date=BUILD_DATE,
        current_date=current_date)
