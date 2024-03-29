from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
# from flask_security import Security, SQLAlchemyUserDatastore
from flask_mail import Mail
from flask_babel import Babel
import os
from logging.handlers import RotatingFileHandler
import logging

from config import Config


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
# security = Security()
mail = Mail()
babel = Babel()


def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(config_class)
	
	db.init_app(app)
	migrate.init_app(app, db)
	login.init_app(app)
	mail.init_app(app)
	babel.init_app(app)

	"""
	app.config['SECURITY_LOGIN_URL'] = 'auth/login'
	app.config['SECURITY_LOGIN_USER_TEMPLATE'] = 'auth/login.html'
	from app.models import User, Role
	user_datastore = SQLAlchemyUserDatastore(db, User, Role)
	Security.init_app(app, datastore=user_datastore)
	"""

	from app.core import bp as bp_core
	app.register_blueprint(bp_core)
	
	from app.auth import bp as bp_auth
	app.register_blueprint(bp_auth, url_prefix='/auth')
	
	from app.expediente import bp as bp_expediente
	app.register_blueprint(bp_expediente, url_prefix='/expediente')
	
	from app.agenda import bp as bp_agenda
	app.register_blueprint(bp_agenda, url_prefix='/agenda')
	
	from app.listin import bp as bp_listin
	app.register_blueprint(bp_listin, url_prefix='/listin')
	
	from app.minutacion import bp as bp_minutacion
	app.register_blueprint(bp_minutacion, url_prefix='/minutacion')
	
	from app.errors import bp as bp_errors  # ERRORS Blueprint
	app.register_blueprint(bp_errors)

	from app.filters import bp as bp_filters  # FILTERS Blueprint
	app.register_blueprint(bp_filters)

	if not app.debug and not app.testing:
		if not os.path.exists('logs'):
			os.mkdir('logs')
		file_handler = RotatingFileHandler('logs/welex.log', maxBytes=10240, backupCount=10)

		file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
		file_handler.setLevel(logging.DEBUG)
		app.logger.addHandler(file_handler)

		app.logger.setLevel(logging.DEBUG)
		app.logger.info('WeLex startup')
	
	return app


@babel.localeselector
def locale_selector():
	return request.accept_languages.best_match(current_app.config['LANGUAGES'])


from app import models
