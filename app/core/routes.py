from flask import render_template, url_for, current_app, flash
from flask_babel import _

from app.core import bp
from app.decorators import active_required, admin_required


@bp.before_app_first_request
def before_first_request():
	current_app.config['SECURITY_LOGIN_URL'] = url_for('auth.login')
	current_app.config['SECURITY_LOGIN_USER_TEMPLATE'] = 'auth/login.html'


"""
@bp.before_request
def before_request():
	return render_template('loading.html')
"""


@bp.route('/')
@active_required
def start():
	events = [
		{
			'id': 6787,
			'type': 'due',
			'visibility': 'public',
			'content': 'Entrega Documentos Juzagado Exp.22/18',
			'author': {
				'first_name': 'Ramón',
				'last_name': 'De Uña'
			}
		},
		{
			'id': 6788,
			'type': 'reminder',
			'visibility': 'private',
			'content': 'Minutar Exp.22/18',
			'author': {
				'first_name': 'Ramón',
				'last_name': 'De Uña'
			}
		}
	]
	return render_template('inicio.html', title=_('Home'), inicio=True, events=events)


@bp.route('/settings')
@active_required
def settings():
	pass


@bp.route('/help')
@active_required
def help():
	pass


@bp.route('/backup')
@admin_required
def backup():
	pass
