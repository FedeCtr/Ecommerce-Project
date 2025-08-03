from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from models import User
from run import db
from werkzeug.security import generate_password_hash

auth_bp = Blueprint('auth', __name__, template_folder='../templates/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Bienvenido, {}!'.format(user.username), 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('shop.product_list'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')
    return render_template('auth/login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form.get('role', 'cliente')  # Por defecto cliente
        if User.query.filter_by(username=username).first():
            flash('El usuario ya existe', 'warning')
        elif User.query.filter_by(email=email).first():
            flash('El email ya está registrado', 'warning')
        else:
            user = User(username=username, email=email, role=role)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash('Usuario registrado correctamente, puedes iniciar sesión.', 'success')
            return redirect(url_for('auth.login'))
    return render_template('auth/register.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada correctamente.', 'success')
    return redirect(url_for('auth.login'))