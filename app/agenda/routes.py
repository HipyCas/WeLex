from flask_login import login_required

from app.decorators import active_required
from app.agenda import bp


@bp.route('/')
@active_required
def start():
    pass
