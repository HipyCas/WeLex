from flask import Blueprint


bp = Blueprint('min', __name__)


from app.minutacion import routes