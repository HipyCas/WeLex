from functools import wraps
from flask import abort, current_app, url_for, redirect
from flask_login import current_user, login_required


def anonymous_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for('core.start'))
        return f(*args, **kwargs)
    return decorated_function


def active_required(f):
    @wraps(f)
    @login_required
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            if not current_user.active:
                abort(401)
        return f(*args, **kwargs)
    return decorated_function


def admin_required(f):
    @wraps(f)
    @login_required
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:# or current_user is not None:
            if not current_user.admin:
                abort(403)
        return f(*args, **kwargs)
    return decorated_function
