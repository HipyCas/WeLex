from flask import render_template
from flask_login import login_required

from app.decorators import active_required
from app.expediente import bp


@bp.route('/')
@active_required
def start():
	return render_template("expedientes.html", title='Expedientes', expedientes=True)
