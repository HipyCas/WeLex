import os
import secrets
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

#random_key = secrets.token_urlsafe()
#random_salt = secrets.SystemRandom().getrandbits(128)


class Config (object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_urlsafe()

    # SQLAlchemy / database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'welex.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
    }

    # Flask-Security
    # SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT') or 329741136734917748598368574161514991107

    # Babel
    LANGUAGES = ['en', 'es_ES']
