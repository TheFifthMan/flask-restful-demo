from flask import Flask,request,g
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from datetime import datetime, timedelta
from authorization import refresh_token
db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(Configuration[config_name])
    db.init_app(app)
    migrate.init_app(app,db)
    
    from .index import index_bp
    app.register_blueprint(index_bp)
    from .auth import auth_bp
    app.register_blueprint(auth_bp)
    from .error import error_bp
    app.register_blueprint(error_bp)
    from .user import user_bp
    app.register_blueprint(user_bp)

    # 配置响应头
    @app.after_request
    def after_request(response):
        # 不建议使用 * 但是在这里无所谓
        response.headers.add('Access-Control-Allow-Origin', '*')
        if g.current_user:
            try:
                if g.current_user.time_expire_time > datetime.now() + timedelta(seconds=1) and g.current_user.time_expire_time < datetime.now() + timedelta(seconds=60):
                    token_expire = datetime.now() + timedelta(seconds=3600)
                    refresh_token(token_expire)
            except Exception as e:
                print(e)

        if request.method == 'OPTIONS':
            response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
            headers = request.headers.get('Access-Control-Request-Headers')
            if headers:
                response.headers['Access-Control-Allow-Headers'] = headers
        return response

    return app