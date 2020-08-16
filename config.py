import os
from dotenv import load_dotenv
import uuid


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

random_key = uuid.uuid4().hex


class Config (object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or random_key

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'welex.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
