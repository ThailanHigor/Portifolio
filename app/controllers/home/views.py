from . import home
from flask import render_template
from app import db

@home.route("/", methods=["GET"])
def index():
    return render_template("home.html")


@home.route("/sobre-mim", methods=["GET"])
def sobre_mim():
    return render_template("sobremim.html")
