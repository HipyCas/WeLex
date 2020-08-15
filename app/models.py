from app import db


class Expediente(db.Model):
	id = db.Column(db.Integer, primary_key=True)
