from flask import render_template, url_for, current_app
from flask_login import login_required

from app.core import bp


@bp.before_app_first_request
def before_first_request():
	current_app.config['SECURITY_LOGIN_URL'] = url_for('auth.login')


@bp.before_request
def before_request():
	return render_template('loading.html')


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
