from app import db,login
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin,db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,index=True)
    password_hash = db.Column(db.String(256))
    email = db.Column(db.String(50),unique=True,index=True)

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
    
    def get_password(self,password):
        return check_password_hash(self.password_hash,password)

