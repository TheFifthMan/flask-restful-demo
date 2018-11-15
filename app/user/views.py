from flask.views import MethodView
from flask import jsonify,request,url_for,g
from app.user.models import User 
from app.authorization import token_auth


class Users(MethodView):
    def get(self):
        # 对象序列化
        page = request.args.get('page',1,type=int)
        per_page = min(request.args.get('per_page',10,type=int),100)
        data = User.to_collection_dict(User.query,page,per_page,'user.get_users')
        return jsonify(data)


class GetUser(MethodView):
    def get(self,user_id):
        user = User.query.filter_by(id=user_id).first()
        if user:
            return jsonify(user.to_dict())
        else:
            return  jsonify({"message":"bad request"}),400
    
class UserProfile(MethodView):
    decorators = [token_auth.login_required]
    def get(self):
        return jsonify(g.current_user.to_dict())