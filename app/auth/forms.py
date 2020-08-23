from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Alias', validators=[DataRequired(), Length(max=32)])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember_username = BooleanField('Recordar alias', default=None)
    remember_me = BooleanField('Recordarme')

    """
    def validate_username(self, username):
        user = User.query.filter_by(alias=username.data).first()
        if user is None:
            raise ValidationError('Cuenta no encontrada')

    def validate_password(self, password):
        user = User.query.filter_by(alias=self.username.data).first()
        if user is not None and user.check_password(password.data):
            raise ValidationError('Contraseña incorrecta')
    """


class RegisterForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    token = StringField('Clave de registro', validators=[DataRequired()])
    remember_user_pass = BooleanField('Recordar alias')
    login_after = BooleanField('Iniciar sesión tras registro')

class RegisterDataForm(FlaskForm):
    username = StringField('Alias', validators=[DataRequired()])
    email = StringField('Correo electrónico', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Nueva contraseña', validators=[DataRequired(), Length(min=8)])
    password_repeat = PasswordField('Repetir contraseña', validators=[DataRequired()])

    def validate_password_repeat(self, password_repeat):
        if not password_repeat.data == self.password.data:
            return ValidationError('Las contraseñas son diferentes')
