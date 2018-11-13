from flask_restful import Resource
from flask_login import login_required,current_user
from flask import request
from .models import Post
from app import db
class Index(Resource):
    def get(self):
        return {"message":"Hello World"}

class Article(Resource):
    decorators = [login_required]
    def post(self):
        title = request.form['title']
        body = request.form['body']
        article = Post(title=title,body=body)
        article.author = current_user
        db.session.add(article)
        db.session.commit()
        return {
            "message":"add article successful."
        }
