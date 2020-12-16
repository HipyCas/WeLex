from flask import render_template, request, url_for, redirect, flash
from flask_babel import _
from werkzeug.urls import url_parse
from datetime import datetime

from app.decorators import active_required
from app.agenda import bp


@bp.route('/')
@active_required
def start():
    date = request.args.get('date', datetime.today().strftime('%Y-%m-%d'), str)
    # TODO: query event by date `date`
    return render_template('agenda.html', title=_('Agenda'), date=date)


event_delete_route = '/delete/<id>'
@bp.route(event_delete_route)
@active_required
def event_delete(id):
    # TODO Redirect to passed url
    flash(f'Deleted event {id} successfully', 'success')
    # Redirect to passed url
    next_page = request.args.get('next')
    return redirect(next_page)
