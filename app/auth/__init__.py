from flask import Blueprint
from flask_restful import Api
auth_bp = Blueprint('auth',__name__)

errors = {
    'UserAlreadyExistsError': {
        'message': "A user with that username already exists.",
        'status': 409,
    },
    'ResourceDoesNotExist': {
        'message': "A resource with that ID no longer exists.",
        'status': 410,
        'extra': "Any extra information you want.",
    },
    "Access Denied": {
        'message': "Please login to access this API",
        'status': 401,
    }
}
api = Api(auth_bp,errors=errors)

from . import views,routes