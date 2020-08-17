from flask import render_template

from app.core import bp


@bp.before_request
def before_request():
	render_template('loading.html')


@bp.route('/')
def start():
	return render_template('expediente.html', title='Inicio', inicio=True)


@bp.route('/settings')
def settings():
	pass


@bp.route('/help')
def help():
	pass
