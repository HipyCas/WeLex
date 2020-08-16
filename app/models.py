from app import db


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
	clientes = db.Column(db.Boolean)  # 0 -> defensa; 1 -> acusación
	fase = db.Column(db.Integer)
	cuantia = db.Column(db.Integer)
	#actuaciones = TODO relationship one-to-many
	

class Actuacion(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	fecha = db.Column(db.Date)
	#autor = db.Column(db.Integer, foreign_key=Usuario.id)
	fase = db.Column(db.String(64))  # TODO relationship new Fase model?
	contenido = db.Column(db.String(160))
	#adjuntos = TODO relationship Adjunto/File/Archivo
	#comunicaciones/notificaciones = TODO relationship Comunicaciones/Notificaciones
	#agenda/calendario = TODO relationship Agenda/Evento


class Evento(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	autor = db.Column(db.Integer, foreign_key=Usuario.id)
	actuacion = db.Column(db.Integer, foreign_key=Actuacion.id)
	visibilidad = db.Column(db.Boolean)  # 0 -> publico; 1 -> privado
	tipo = db.Column(db.String(12)). # TODO relationship new TipoEvento model
	contenido = db.Column(db.String(160))