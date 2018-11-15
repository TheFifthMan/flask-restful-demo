from flask_httpauth import HTTPBasicAuth,HTTPTokenAuth
from app.user.models import User
from flask import g,abort

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

@basic_auth.verify_password
def verify_password(username,password):
    user = User.query.filter_by(username=username).first()
    if not user or not user.get_password(password):
        return False
    g.current_user = user
    return True

@basic_auth.error_handler
def error_handler():
    abort(401)

@token_auth.verify_token
def verify_token(token):
    g.current_user = User.check_token(token) if token else None
    return g.current_user is not None

@token_auth.error_handler
def error_handler():
    abort(401)
    