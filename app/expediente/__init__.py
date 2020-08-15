from flask import Blueprint


bp = Blueprint('exp', __name__)


from app.expediente import routes