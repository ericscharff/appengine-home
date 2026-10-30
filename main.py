import secrets
from datetime import datetime, timedelta, timezone

from flask import Flask, make_response, render_template, request

app = Flask(__name__)

BUILD_DATE = "Last modified Fri Oct 30 07:36:30 AM MDT 2026"


@app.after_request
def add_static_headers(response):
    if request.path.startswith("/static/"):
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Cross-Origin-Resource-Policy"] = "cross-origin"
        response.headers["Cross-Origin-Embedder-Policy"] = "require-corp"
        response.headers["Cross-Origin-Opener-Policy"] = "same-origin"
    return response


@app.route("/calc")
def calc_main():
    return render_template("calc/index.html")


@app.route("/homeapp")
@app.route("/homeapp/")
def homeapp_main():
    current_date = (datetime.now(timezone.utc) + timedelta(hours=-6)).isoformat()
    return render_template("homeapp/index.html", current_date=current_date)


@app.route("/homeapp/clock")
def homeapp_clock():
    return render_template("homeapp/clock.html")


@app.route("/homeapp/runner")
def homeapp_runner():
    return render_template("homeapp/runner.html")


@app.route("/check_token")
def check_update():
    message = f"Your token was {request.args.get('token', 'nothing')}."
    return {"message": message, "next_token": secrets.token_urlsafe(16)}


@app.route("/")
def root():
    current_date = (datetime.now(timezone.utc) + timedelta(hours=-6)).isoformat()
    return render_template(
        "index.html", build_date=BUILD_DATE, current_date=current_date
    )
