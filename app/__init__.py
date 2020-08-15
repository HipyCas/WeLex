from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
#from flask_babel import Babel

from config import Config


db = SQLAlchemy()
migrate = Migrate()
#login = LoginManager()
#login.login_view = 'auth.login'
mail = Mail()
#babel = Babel()

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(config_class)
	
	db.init_app(app)
	migrate.init_app(app, db)
#	login.init_app(app)
	mail.init_app(app)
	
	from app.core import bp as bp_core
	app.register_blueprint(bp_core)
	
	from app.expediente import bp as bp_expediente
	app.register_blueprint(bp_expediente, url_prefix='expedientes')
	
	from app.agenda import bp as bp_agenda
	app.register_blueprint(bp_expediente, url_prefix='agenda')
	
	return app


from app import models
