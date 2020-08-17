from flask import render_template
from flask_login import login_required

from app.core import bp


@bp.before_request
def before_request():
	render_template('loading.html')


@bp.route('/')
@login_required
def start():
	return render_template('inicio.html', title='Inicio', inicio=True)


@bp.route('/settings')
@login_required
def settings():
	pass


@bp.route('/help')
@login_required
def help():
	pass
