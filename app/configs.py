import os

class Release(object):
    SITE_NAME                   = 'Tharsis frontend'
    SERVER_NAME                 = os.environ.get('SERVER_NAME')
    SECRET_KEY                  = os.environ.get('SECRET_KEY')
    SQL_ALCHEMY_DATABASE_URI    = os.environ.get('DATABASE_URI')

class Dev(Release):
    DEBUG                       = True
    SECRET_KEY                  = 'my_53cr3t_k3y'
    SQL_ALCHEMY_DATABASE_URI    = 'oracle://606060545:lliw@datalab1.zion.bt.co.uk/orpm'

class Test(Release):
    TESTING                     = True
