from flask import Blueprint


bp = Blueprint('agenda', __name__)


from app.agenda import routes
