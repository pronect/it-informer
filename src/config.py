import os


class Config():
    POSTGRES_DB = os.getenv('POSTGRES_DB', 'it_informer')
    POSTGRES_USER = os.getenv('POSTGRES_USER', 'it_informer')
    POSTGRES_PASS = os.getenv('POSTGRES_PASS', 'it_informer')
    POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5431')
    SQLALCHEMY_DATABASE_URI = 'postgres://it_informer:it_informer@localhost/it_informer'
    TRACK_MODIFICATIONS = False

    SLACK_TOKEN = 0
    SLACK_CHANEL = 0

    FLASK_DEBUG = True
    FLASK_HOST = '0.0.0.0'

    TRACK_MODIFICATIONS = False
    SECRET_KEY = 0
