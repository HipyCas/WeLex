from flask import render_template

from app.expediente import bp


@bp.route('/')
def start():
	return render_template("expedientes.html", title='Expedientes', expedientes=True)