from . import user_bp
from .views import Users,GetUser,UserProfile
user_bp.add_url_rule('/get_users',view_func=Users.as_view('get_users'))
user_bp.add_url_rule('/user/<int:user_id>',view_func=GetUser.as_view('get_user'))
user_bp.add_url_rule('/user/profile',view_func=UserProfile.as_view('user_profile'))