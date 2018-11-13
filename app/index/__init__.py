from flask import Blueprint
from flask_restful import Api
index_bp = Blueprint('index',__name__)
api = Api(index_bp)
from . import views,routes
