from app import db
#from app.auth.models import User

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(256))
    body = db.Column(db.Text)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
