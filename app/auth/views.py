from flask import request,abort,jsonify,url_for,g
from app.user.models import User
from app import db,auth
from flask.views import MethodView
from app.authorization import basic_auth
from datetime import datetime,timedelta
       
class Register(MethodView):
    def post(self):
        data = request.get_json() or {}
        if "username" not in data or "email" not in data or 'password1' not in data or 'password2' not in data:
            return jsonify({"message":"please fill with username/email/password1/password2"}),400
        
        if data['password1'] != data['password2']:
            return jsonify({"message":"bad request0"}),400
        
        if User.query.filter_by(username=data['username']).first():
            return jsonify({'message':"bad request1"}),409
        
        if User.query.filter_by(email=data['email']).first():
            return jsonify({'message':"bad request2"}),409
        
        user = User()
        user.from_dict(data,new_user=True)
        db.session.add(user)
        db.session.commit()
        response = jsonify(user.to_dict())
        response.status_code=201
        response.headers['Location'] = url_for('user.get_user',user_id=user.id)
        return response

class Token(MethodView):
    decorators=[basic_auth.login_required]
    def get(self):
        token_expiration = datetime.now() + timedelta(seconds=3600)
        token = g.current_user.generate_token(token_expiration)
        db.session.commit()
        return jsonify({
            "token": token
        })
    
    def delete(self):
        g.current_user.token_expire_time = datetime.now() - timedelta(seconds=1)
        db.session.commit()
        return jsonify({
            "message":"delete token"
        })


# class Refresh_token(MethodView):
#     decorators = [basic_auth.login_required]
#     def get(self):
#         pass