from . import api
from .views import Register,UserProfile,Login,Logout
api.add_resource(Register,'/register')
api.add_resource(UserProfile,'/profile')
api.add_resource(Login,'/login')
api.add_resource(Logout,'/logout')