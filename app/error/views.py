from . import error_bp
from flask import jsonify

@error_bp.app_errorhandler(404)
def page_not_found(error):
    return jsonify({"message":"Not Found"}),404

@error_bp.app_errorhandler(500)
def server_down(error):
    return jsonify({"message":"Internal Error"}),500

@error_bp.app_errorhandler(401)
def server_down(error):
    return jsonify({"message":"Unauthorized"}),401