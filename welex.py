from app import create_app, cli, db, mail
from app.models import RegistrationToken, User, Expediente, Actuacion, Evento


app = create_app()
cli.register(app)


@app.shell_context_processors
def make_shell_context():
    return {'app': app, 'db': db, 'mail': mail, 'RegistrationToken': RegistrationToken, 'User': User, 'Expediente': Expediente, 'Actuacion': Actuacion, 'Evento': Evento}
