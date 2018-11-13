class Config(object):
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:qwe123@127.0.0.1/restful"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY = '1fa1db43-20a2-40ec-ae01-b7e27e390306'

class DevConfig(Config):
    pass

class ProdConfig(Config):
    pass

Configuration = {
    'dev': DevConfig,
    'prod': ProdConfig
}