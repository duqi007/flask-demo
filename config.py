import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_RUL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMIN = os.environ.get('ADMIN')
    POSTS_PER_PAGE = 3
    LANGUAGES = ['zh','en','es']
    BD_TRANSLATOR_KEY = os.environ.get('BD_TRANSLATOR_KEY')
    BD_APP_ID = os.environ.get('BD_APP_ID')
    TRANSLATE_URL = os.environ.get('TRANSLATE_URL')
    # ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')