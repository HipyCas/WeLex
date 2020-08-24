from flask import render_template, flash, url_for, redirect, request
from flask_login import login_user, logout_user, login_required, current_user
from flask_babel import _
from werkzeug.urls import url_parse

from app.decorators import admin_required
from app.auth import bp
from app.auth.forms import *
from app.models import User
from app.utils import secondsTrimester


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('core.start'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(alias=form.username.data).first()
        if user is None:
            flash(_('User not found'), category='danger')
            return render_template('auth/login.html', title=_('Login'), form=form)
        if not user.check_password(form.password.data):
            flash(_('Wrong password'), category='danger')
            return render_template('auth/login.html', title=_('Login'), form=form)
        if not user.active:
            flash(_('User is deactivated'), category='danger')
            return render_template('auth/login.html', title=_('Login'), form=form)
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('core.start')
        return redirect(next_page)
    form.username.default = request.cookies.get('WeLex-alias')
    form.process()
    if str(request.cookies.get('WeLex-recordar-alias')) == "1":
        form.remember_username.active = True
    else:
        form.remember_username.active = False
    return render_template('auth/login.html', title=_('Login'), form=form, cookie_save_username=True)


@bp.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect(url_for('core.start'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('core.start'))
    form = RegisterForm()
    if form.validate_on_submit():
        # TODO: validate token (logic)
        login_user(User.query.get(1))
        return redirect(url_for('auth.register_data', save_username=form.remember_username.data, login=form.login_after.data))
    return render_template('auth/register.html', title=_('Register'), form=form)


@bp.route('/register/data', methods=['GET', 'POST'])
@login_required
def register_data():
    form = RegisterDataForm()
    if form.validate_on_submit():
        # TODO logic
        # current_user.alias = form.username.data
        # current_user.email = form.email.data
        # current_user.set_password(form.password.data)
        # db.session.commit()
        if request.args.get('save_username', False, type=bool):
            request.cookies.set_cookie('WeLex-alias', current_user.username, secondsTrimester)
            #request.cookies.set_cookie('WeLex-contrasena', form.password.data, 60*60*24*31)
            request.cookies.set_cookie('WeLex-recordar-alias', request.args.get('save_username', False, type=bool), secondsTrimester)
        keep_login = request.args.get('login', False, type=bool)
        if not keep_login:
            logout_user()
        return redirect(url_for('core.start'))
    return render_template('auth/register_data.html', title=_('Complete registration'), form=form)


@bp.route('/manage')
@admin_required
def users():
    return render_template('auth/users.html', title=_('Users'))


@bp.route('/manage/add')
@admin_required
def add_user():
    return render_template('auth/users.html', title=_('New user'))


# TODO: Recover password? A page to recover it with e.g. an email or a page to show info saying to ask an admin to let you change it
