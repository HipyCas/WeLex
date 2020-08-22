from flask import render_template

from app import db
from app.errors import bp


# 400 - 499 : Client errors

@bp.app_errorhandler(400)
def bad_request(error):
    return render_template('errors/400.html', title='400')


@bp.app_errorhandler(401)
def unauthorized(error):
    return render_template('errors/401.html', title='401')


"""
@bp.app_errorhandler(402)
def payment_required(error):
    return render_template('errors/401.html', title='402')
"""


@bp.app_errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html', title='403')


@bp.app_errorhandler(404)
def not_found(error):
    return render_template('errors/404.html', title='404')


@bp.app_errorhandler(405)
def method_not_allowed(error):
    return render_template('errors/405.html', title='405')


@bp.app_errorhandler(406)
def not_acceptable(error):
    return render_template('errors/406.html', title='406')


"""
@bp.app_errorhandler(407)
def proxy_authentication_required(error):
    return render_template('errors/407.html', title='507')
"""


# 500 - 599 : Server errors

@bp.app_errorhandler(500)
def internal_server_error(error):
    db.session.rollback()
    return render_template('errors/500.html', title='500')
