from flask import Blueprint, render_template

static = Blueprint("main", __name__)

@static.route("/")
def main():
    return render_template("index.html")

@static.route("/about")
def about():
    return render_template("about.html")

@static.route("/nextinfo")
def nextpage():
    return render_template("next.html")

@static.route("/feature")
def feature():
    return render_template("features.html")