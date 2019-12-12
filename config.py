import os



class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY ='c00l%K3y'
    # SECURITY_PASSWORD_SALT= 'c00l%K3yS4lt'

    SQLALCHEMY_DATABASE_URI= 'postgresql://tpostgres:password123@localhost/Monthly_Bills'
    SQLALCHEMY_TRACK_MODIFICATIONS= False
 
class Development(Config):
    DEBUG = True


class Production(Config):
    pass


class Testing(Config):
    TESTING = True