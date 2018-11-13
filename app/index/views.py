from flask_login import login_required,current_user
from flask import request,jsonify
from .models import Post
from app import db
from flask.views import MethodView

class Index(MethodView):
    def get(self):
        return jsonify({"message":"Hello World"})

class Article(MethodView):
    decorators = [login_required]
    def post(self):
        title = request.form['title']
        body = request.form['body']
        article = Post(title=title,body=body)
        article.author = current_user
        db.session.add(article)
        db.session.commit()
        return jsonify({
            "message":"add article successful."
        })
