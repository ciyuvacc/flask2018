class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    HOST = '0.0.0.0' 
    PORT = '8888'
    DEBUG = True
