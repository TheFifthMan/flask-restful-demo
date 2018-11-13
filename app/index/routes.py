from . import index_bp
from .views import Index,Article
index_bp.add_url_rule('/',view_func=Index.as_view('index'))
index_bp.add_url_rule('/post/article',view_func=Article.as_view('post_article'))