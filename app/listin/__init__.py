from flask import Blueprint


bp = Blueprint('list', __name__)


from app.listin import routes
