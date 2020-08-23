from app import create_app, db
from app.models import User

app = create_app()
app.app_context().push()

name = str(input('Name: '))
username = str(input('Username: '))
email = str(input('Email: '))
password = str(input('Password: '))
admin = bool(input('Admin (True/False): '))

u = User(alias=username, email=email, nombre=name, admin=admin, active=True)
u.set_password(password)
db.session.add(u)
db.session.commit()
