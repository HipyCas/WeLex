from flask import render_template, flash, url_for, redirect, request
from flask_login import login_user, logout_user, login_required, current_user
from flask_babel import _
from werkzeug.urls import url_parse
from uuid import uuid4

from app import db
from app.decorators import admin_required, anonymous_required
from app.auth import bp
from app.auth.forms import *
from app.models import User, RegistrationToken
from app.utils import secondsTrimester


@bp.route('/login', methods=['GET', 'POST'])
@anonymous_required
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(alias=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(_('User or password is incorrect'), category='danger')
            return render_template('auth/login.html', title=_('Login'), form=form)
        if not user.active:
            flash(_('User is deactivated'), category='danger')
            return render_template('auth/login.html', title=_('Login'), form=form)
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('core.start')
        flash(_('Successfully logged in'), 'success')
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
@anonymous_required
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # TODO: validate token (logic)
        token = RegistrationToken.query.filter_by(token=form.token.data).first()
        if token is None:
            flash(_('Token not found'), category='danger')
            return render_template('auth/register.html', title=_('Register'), form=form)
        if token.target_name != form.name.data:
            flash(_('Token and name do not match'), category='danger')
            return render_template('auht/register.html', title=_('Register'), form=form)
        user = User(nombre=form.name.data, registration_token_id=token.id, active=False, admin=False)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('auth.register_data', save_username=form.remember_user_pass.data, login=form.login_after.data))
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
    users = User.query.all()
    tokens = RegistrationToken.query.all()
    return render_template('auth/users.html', title=_('Users'), users=users, tokens=tokens)


@bp.route('/manage/add', methods=['GET', 'POST'])
@admin_required
def add_user():
    form = AddUserForm()
    if form.validate_on_submit():
        user = User.query.filter_by(alias=form.username.data).first()
        if user is not None:
            flash(_('Username is already taken'))
            return render_template('auth/add_user.html', title=_('Add user'), form=form)
        user = User.query.filter_by(nombre=form.name.data).first()
        if user is not None:
            flash(_('Name is already registered'))
            return render_template('auth/add_user.html', title=_('Add user'), form=form)
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            flash(_('Email is already registered'))
            return render_template('auth/add_user.html', title=_('Add user'), form=form)
        del user
        while True:
            token = uuid4().hex
            existing_token = RegistrationToken.query.filter_by(token=token).first()
            if existing_token is None:
                break
        tokenDB = RegistrationToken(target_name=form.name.data, token=token)
        db.session.add(tokenDB)
        db.session.commit()
        flash(_('Token successfully created'))
        return redirect(url_for('auth.users'))
    return render_template('auth/add_user.html', title=_('Add user'), form=form)


# TODO: Recover password? A page to recover it with e.g. an email or a page to show info saying to ask an admin to let you change it
