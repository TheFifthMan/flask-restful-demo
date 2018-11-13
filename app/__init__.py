from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_httpauth import HTTPBasicAuth
from flask_login import LoginManager
db = SQLAlchemy()
# auth = HTTPBasicAuth()
migrate = Migrate()
login = LoginManager()
login.session_protection = "strong"

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(Configuration[config_name])
    db.init_app(app)
    migrate.init_app(app,db)
    login.init_app(app)
    from .index import index_bp
    app.register_blueprint(index_bp)
    from .auth import auth_bp
    app.register_blueprint(auth_bp)
    from .error import error_bp
    app.register_blueprint(error_bp)

    return app