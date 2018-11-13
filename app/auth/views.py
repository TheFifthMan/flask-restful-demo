from flask import request,abort,jsonify
from .models import User
from app import db,auth
from flask_login import login_user,login_required,current_user,logout_user
from flask.views import MethodView

class Login(MethodView):
    def post(self):
        if not current_user.is_authenticated:
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(username=username).first()
            if user and user.get_password(password):
                login_user(user)
            else:
                return jsonify({"message":"Login failed"})
        return jsonify({"message":"Login successful"})

class Logout(MethodView):
    def get(self):
        if current_user.is_authenticated:
            logout_user()
        
        return jsonify({"message": 'logout successful'})
       
class Register(MethodView):
    def post(self):
        if not current_user.is_authenticated:
            try:
                username = request.form['username']
                password = request.form['password1']
                password2 = request.form['password2']
                email = request.form['email']
                if password != password2:
                    return jsonify({"message":"password don't match!"})
                user = User.query.filter_by(username=username).first()
                if not user:
                    user = User(username=username,email=email)
                    user.set_password(password)
                    db.session.add(user)
                    db.session.commit()
                    return jsonify({"message":"register successful!"})
            
            except Exception as e:
                db.session.rollback()

        return jsonify({"message":"register failed"})


class UserProfile(MethodView):
    decorators = [login_required]
    def get(self):
        return jsonify({
            "username":current_user.username,
            "email":current_user.email
        })
    