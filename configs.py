import os

class Release(object):
    SITE_NAME                   = 'Tharsis frontend'
    SERVER_NAME                 = os.environ.get('SERVER_NAME')
    SECRET_KEY                  = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI    = os.environ.get('DATABASE_URI')

class Dev(Release):
    DEBUG                       = True
    SECRET_KEY                  = 'my_53cr3t_k3y'
    SQLALCHEMY_DATABASE_URI    = 'sqlite:///test.db'

class Test(Release):
    TESTING                     = True
    SQLALCHEMY_DATABASE_URI    = 'sqlite:///test.db'

