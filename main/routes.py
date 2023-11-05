from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("home.html", title = "Home")

@main.route("/experiment")
def experiment():
    return render_template("experiment.html", title = "P")