from flask import render_template, request
from flask_babel import _
from datetime import datetime

from app.decorators import active_required
from app.agenda import bp


@bp.route('/')
@active_required
def start():
    date = request.args.get('date', datetime.today().strftime('%Y-%m-%d'), str)
    # TODO: query event by date `date`
    return render_template('agenda.html', title=_('Agenda'), date=date)
