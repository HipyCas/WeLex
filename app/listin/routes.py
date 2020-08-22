from flask_login import login_required

from app.listin import bp


@bp.route('/')
@login_required
def start():
    pass
