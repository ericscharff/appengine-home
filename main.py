import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/calc/")
def calc_main():
    return render_template("calc/index.html")

@app.route("/calc/index.html")
def calc_index():
    return render_template("calc/index.html")

@app.route("/calc/manifest.json")
def calc_manifest():
    return render_template("calc/manifest.json")

@app.route("/homeapp/")
def homeapp_main():
    return render_template("homeapp/index.html")

@app.route("/homeapp/index.html")
def homeapp_index():
    return render_template("homeapp/index.html")

@app.route("/homeapp/manifest.json")
def homeapp_manifest():
    return render_template("homeapp/manifest.json")

@app.route("/")
def root():
    return render_template("index.html")
