from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    from .controllers.home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .controllers.blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint)

    from .controllers.projetos import projetos as projetos_blueprint
    app.register_blueprint(projetos_blueprint)
    
    return app