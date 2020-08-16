from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Alias', validators=[DataRequired(), Length(max=32)])
    password = PasswordField('Contraseña', validators=[DataRequired()])
