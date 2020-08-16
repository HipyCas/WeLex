from flask import Blueprint


bp = Blueprint('auth', __name__)#subdomain='auth')


from app.auth import routes