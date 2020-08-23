from functools import wraps
from flask import abort, current_app
from flask_login import current_user, login_required


def admin_required(f):
    @wraps(f)
    @login_required
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:# or current_user is not None:
            if not current_user.admin:
                abort(403)
        return f(*args, **kwargs)
    return decorated_function
