from app import create_app, db
from app.models import User


name = str(input('Name: '))
username = str(input('Username: '))
email = str(input('Email: '))
password = str(input('Password: '))

create_app().app_context().push()
u = User(alias=username, email=email, nombre=name)
u.set_password(password)
db.session.add(u)
db.session.commit()
