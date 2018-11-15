from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask import url_for
from datetime import datetime,timedelta
import base64
import os 

class PagenationAPIMixin(object):
     @staticmethod
     def to_collection_dict(query,page,per_page,endpoint,**kwargs):
         resources = query.paginate(page,per_page,False)
         data = {
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
    token = db.Column(db.String(32))
    token_expire = db.Column(db.DateTime)

    def get_token(self,expires_in=3600):
        now = datetime.now()
        if self.token and self.token_expire > now + timedelta(seconds=60):
            return self.token 
        
        self.token= base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expire = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token
    
    def revoke_token(self):
        self.token_expire = datetime.now() - timedelta(seconds=1)
    
    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if not user or user.token_expire < datetime.now():
            return None
        
        return user

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
    
    def get_password(self,password):
        return check_password_hash(self.password_hash,password)



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

