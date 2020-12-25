from flask import Blueprint


bp = Blueprint('agen', __name__)


from app.agenda import routes
