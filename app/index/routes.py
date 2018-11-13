from . import api
from .views import Index,Article
api.add_resource(Index,'/')
api.add_resource(Article,'/post-article')