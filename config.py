import os

class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Amoamati1.@localhost/bes_ecomm'
    CACHE_TYPE = 'SimpleCache'
    DEBUG = True

class ProductionConfig:
    DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    CACHE_TYPE = 'SimpleCache'
    DEBUG = False