from flask_login import login_required

from app.minutacion import bp


@bp.route('/')
@login_required
def start():
    pass
