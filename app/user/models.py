from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask import url_for,current_app
from datetime import datetime,timedelta
import base64
import os 
import jwt

class PagenationAPIMixin(object):
     @staticmethod
     def to_collection_dict(query,page,per_page,endpoint,**kwargs):
         resources = query.paginate(page,per_page,False)
         data = {
             # 这里的resources.items是一个list,包含了所有的user
             "users":[item.to_dict() for item in resources.items],
              '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
            },
            '_links': {
                'self': url_for(endpoint, page=page, per_page=per_page,
                                **kwargs),
                'next': url_for(endpoint, page=page + 1, per_page=per_page,
                                **kwargs) if resources.has_next else None,
                'prev': url_for(endpoint, page=page - 1, per_page=per_page,
                                **kwargs) if resources.has_prev else None
            }
         }
         return data

class User(PagenationAPIMixin,db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,index=True)
    password_hash = db.Column(db.String(256))
    email = db.Column(db.String(50),unique=True,index=True)
    posts = db.relationship('Post',backref='author',lazy='dynamic')
    token = db.Column(db.String(500))

    # 有点重复的功能
    token_expire_time = db.Column(db.DateTime)

    def generate_token(self,token_expiration):
        try:
            payload = {
                'exp': token_expiration,
                'iss': 'ken',
                'data': {
                    'id': self.id,
                },
                'iat':datetime.now(),
            }
            self.token = jwt.encode(
                payload,
                current_app.config['SECRET_KEY'],
                algorithm='HS256'
            ).decode('utf-8')
            self.token_expire_time = token_expiration
            return self.token
        except Exception as e:
            print(e)
            return e

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
    
    def get_password(self,password):
        return check_password_hash(self.password_hash,password)


    # 序列化
    def to_dict(self):
        data =  {
            "id": self.id,
            "username":self.username,
            "email": self.email
        }

        return data

    # 反序列化
    def from_dict(self,data,new_user=False):
        for field in ['username','email']:
            if field in data:
                setattr(self,field,data[field])
        
        if new_user and 'password1' in data:
            self.set_password(data['password1'])

    def __str__(self):
        return "<user :{}>".format(self.username)