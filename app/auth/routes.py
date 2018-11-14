from . import auth_bp
from .views import Register
auth_bp.add_url_rule('/register',view_func=Register.as_view('register'))
