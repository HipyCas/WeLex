from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
#from flask_babel import Babel

from config import Config


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
mail = Mail()
#babel = Babel()

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(config_class)
	
	db.init_app(app)
	migrate.init_app(app, db)
	login.init_app(app)
	mail.init_app(app)
	
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
	
	return app


from app import models
