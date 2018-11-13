from app  import create_app,db
app = create_app('dev')

from app.auth.models import User
from app.index.models import Post

@app.shell_context_processor
def shell_context_processor():
    return {'db':db,'User':User,"Post":Post}