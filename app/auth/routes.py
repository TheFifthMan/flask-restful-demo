from . import auth_bp
from .views import Register,Token
auth_bp.add_url_rule('/register',view_func=Register.as_view('register'))
auth_bp.add_url_rule('/token',view_func=Token.as_view('token'))