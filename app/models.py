from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	alias = db.Column(db.String(32), unique=True, index=True)
	email = db.Column(db.String(140), unique=True, index=True)
	nombre = db.Column(db.String(24))
	apellidos = db.Column(db.String(48))
	password_hash = db.Column(db.String)
	registration_token_id = db.Column(db.Integer, db.ForeignKey('registration_tokens.id'))
	registration_token = db.relationship('RegistrationToken', back_populates="user")
	registration_tokens = db.relationship('RegistrationToken', backref='dispatcher', lazy='dynamic')

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, check):
		return check_password_hash(self.password_hash, check)


class RegistrationToken(db.Model):
	__tablename__ = 'registration_tokens'
	id = db.Column(db.Integer, primary_key=True)
	token = db.Column(db.String, unique=True, index=True)
	target_name = db.Column(db.String, unique=True, index=True)
	target = db.relationship("User", uselist=False, back_populates="registration_token")
	dispatcher_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Expediente(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	numero = db.Column(db.Integer)
	ano = db.Column(db.Integer)
	autos_numero = db.Column(db.Integer)
	autos_ano = db.Column(db.Integer)
	juzgado = db.Column(db.String(256))
	#abogados = TODO many-to-many relationship
	#demandados = TODO many-to-many relationship
	#demandantes = TODO many-to-many relationship
	clientes = db.Column(db.Integer)  # 0 -> defensa; 1 -> acusación
	fase = db.Column(db.Integer)
	cuantia = db.Column(db.Integer)
	#actuaciones = TODO relationship one-to-many
	

class Actuacion(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	fecha = db.Column(db.Date)
	#autor = db.Column(db.Integer, foreign_key=User.id)
	fase = db.Column(db.String(64))  # TODO relationship new Fase model?
	contenido = db.Column(db.String(160))
	#adjuntos = TODO relationship Adjunto/File/Archivo
	#comunicaciones/notificaciones = TODO relationship Comunicaciones/Notificaciones
	#agenda/calendario = TODO relationship Agenda/Evento


class Evento(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	autor = db.Column(db.Integer, db.ForeignKey('user.id'))
	actuacion = db.Column(db.Integer, db.ForeignKey('actuacion.id'))
	visibilidad = db.Column(db.Integer)  # 0 -> publico; 1 -> privado
	tipo = db.Column(db.String(12))  # TODO relationship new TipoEvento model
	contenido = db.Column(db.String(160))


@login.user_loader
def load_user(id):
	return User.query.get(int(id))
