from flask_restful import Resource
from flask import request
from .models import User
from app import db,auth
from flask_login import login_user,login_required,current_user,logout_user

class Login(Resource):
    def post(self):
        if not current_user.is_authenticated:
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(username=username).first()
            if user and user.get_password(password):
                login_user(user)
            else:
                return {"message":"Login failed"}
        
        return {"message":"Login successful"}

class Logout(Resource):
    def get(self):
        if current_user.is_authenticated:
            logout_user()
        
        return {"message": 'logout successful'}
       
class Register(Resource):
    def post(self):
        if not current_user.is_authenticated:
            username = request.form['username']
            password = request.form['password1']
            password2 = request.form['password2']
            email = request.form['email']
            if password != password2:
                return {"message":"password don't match!"}
            user = User.query.filter_by(username=username).first()
            if not user:
                user = User(username=username,email=email)
                user.set_password(password)
                db.session.add(user)
                db.session.commit()
                return {"message":"register successful!"}
        
        return {"message":"register failed"}


class UserProfile(Resource):
    decorators = [login_required]
    def get(self):
        return {
            "username":current_user.username,
            "email":current_user.email
        }
    