from flask import render_template
from flask_security import login_required

from app.expediente import bp


@bp.route('/')
@login_required
def start():
	return render_template("expedientes.html", title='Expedientes', expedientes=True)