from flask import render_template, flash
from flask_login import login_user

from app.auth import bp
from app.auth.forms import *
from app.models import User


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(alias=form.user.username).first()
        if user is None:
            flash('Usuario no encontrado', category='danger')
            return render_template('auth/login.html', form=form)
        if not user.check_password(form.password.data):
            flash('Contraseña incorrecta', category='danger')
            return render_template('auth/login.html', form=form)
        login_user(user)
    return render_template('auth/login.html', form=form)

