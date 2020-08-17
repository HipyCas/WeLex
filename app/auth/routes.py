from flask import render_template, flash, url_for, redirect
from flask_login import login_user, logout_user, login_required, current_user

from app.auth import bp
from app.auth.forms import *
from app.models import User


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('core.start'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(alias=form.username.data).first()
        if user is None:
            flash('Usuario no encontrado', category='danger')
            return render_template('auth/login.html', form=form)
        if not user.check_password(form.password.data):
            flash('Contraseña incorrecta', category='danger')
            return render_template('auth/login.html', form=form)
        login_user(user)
        return redirect(url_for('core.start'))
    return render_template('auth/login.html', form=form)


@bp.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect(url_for('core.start'))


@bp.route('/manage')
@login_required
def users():
    pass
