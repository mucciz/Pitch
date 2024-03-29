
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://deathstar:deathstar@localhost/pitch'

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options ={"production":ProdConfig,"default":DevConfig,"testing":TestConfig}

