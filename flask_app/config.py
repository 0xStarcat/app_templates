import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    if os.environ.get('FLASK_ENV') == 'production':
        MONGO_URI = os.environ.get('DATABASE_URL')
        ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
        MAIL_SERVER = os.environ.get('MAIL_SERVER')
        MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
        MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
        MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
        MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
        ADMINS = ['']
    elif os.environ.get('FLASK_ENV') == 'development':
        MONGO_URI = os.environ.get('DEV_DATABASE_URL')
        ELASTICSEARCH_URL = os.environ.get('DEV_ELASTICSEARCH_URL')
    pass
