from . import projetos
from flask import render_template
from app import db

@projetos.route("/portfolio", methods=["GET"])
def index():
    return render_template("projetos/index.html")

@projetos.route("/projetos/projeto1", methods=["GET"])
def detalhes():
    return render_template("projetos/detalhes.html")
