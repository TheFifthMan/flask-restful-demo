from flask import Blueprint
from flask_restful import Api
error_bp = Blueprint('error',__name__)
api = Api(error_bp)
