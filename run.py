from app  import create_app
app = create_app('dev')

from app.auth import models
from app.index import models

