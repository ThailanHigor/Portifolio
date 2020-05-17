from . import blog
from flask import render_template
from app import db


@blog.route("/blog", methods=["GET"])
def index():
    return render_template("blog/index.html")

@blog.route("/blog/post1", methods=["GET"])
def detalhes():
    return render_template("blog/detalhes.html")
