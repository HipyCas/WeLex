from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError


class LoginForm(FlaskForm):
    username = StringField('Alias', validators=[DataRequired(), Length(max=32)])
    password = PasswordField('Contraseña', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    token = StringField('Clave de registro', validators=[DataRequired()])

class RegisterDataForm(FlaskForm):
    username = StringField('Alias', validators=[DataRequired()])
    email = StringField('Correo electrónico', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Nueva contraseña', validators=[DataRequired(), Length(min=8)])
    password_repeat = PasswordField('Repetir contraseña', validators=[DataRequired()])

    def validate_password_repeat(self, password_repeat):
        if not password_repeat.data == self.password.data:
            return ValidationError('Las contraseñas son diferentes')
