import datetime
import random

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/calc/")
@app.route("/calc/index.html")
def calc_main():
    return render_template("calc/index.html")

@app.route("/calc/manifest.json")
def calc_manifest():
    return render_template("calc/manifest.json")

@app.route("/homeapp/")
@app.route("/homeapp/index.html")
def homeapp_main():
    roll = random.randint(1, 20)
    return render_template("homeapp/index.html", diceroll=roll)

@app.route("/homeapp/manifest.json")
def homeapp_manifest():
    return render_template("homeapp/manifest.json")

@app.route("/")
def root():
    return render_template("index.html")
