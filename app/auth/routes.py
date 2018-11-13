from . import auth_bp
from .views import Register,UserProfile,Login,Logout
auth_bp.add_url_rule('/register',view_func=Register.as_view('register'))
auth_bp.add_url_rule('/profile',view_func=UserProfile.as_view('profile'))
auth_bp.add_url_rule('/login',view_func=Login.as_view('login'))
auth_bp.add_url_rule('/logout',view_func=Logout.as_view('logout'))