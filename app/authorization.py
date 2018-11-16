from flask_httpauth import HTTPTokenAuth,HTTPBasicAuth
from flask import g,abort,current_app
from app.user.models import User
import jwt
from datetime import datetime,timedelta
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
    try:
        payload = jwt.decode(token, current_app.config['SECRET_KEY'])
        if ('data' in payload and 'id' in payload['data']):
            u = User.query.filter_by(id=payload['data']['id']).first()
            if u and u.token_expire_time >= datetime.now() + timedelta(seconds=60):
                g.current_user = u
                return True
    except Exception as e:
        print(e)
        abort(400)
    
    return False

@token_auth.error_handler
def token_error_handler():
    abort(401)


def refresh_token(token):
    user = User.query.filter_by(token=token).first()
    if user:
        token_expire = datetime.now() + timedelta(seconds=600)
        user.generate_token(token_expire)
        db.session.commit()
