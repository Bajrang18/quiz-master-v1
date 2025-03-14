from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from models import db, User
from datetime import datetime
import re

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def index():
    if current_user.is_authenticated:
        if current_user.is_admin:
            return redirect(url_for('admin.dashboard'))
        else:
            return redirect(url_for('user.dashboard'))
    return render_template('index.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('admin.dashboard') if user.is_admin else url_for('user.dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        full_name = request.form.get('full_name')
        qualification = request.form.get('qualification')
        dob_str = request.form.get('dob')

        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", username):
            flash('Invalid email format.', 'danger')
            return render_template('register.html')

        # Check if username already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists. Try another one.', 'danger')
            return render_template('register.html')

        # Validate password length
        if len(password) < 6:
            flash('Password must be at least 6 characters.', 'danger')
            return render_template('register.html')

        # Validate date format
        try:
            dob = datetime.strptime(dob_str, '%Y-%m-%d').date() if dob_str else None
        except ValueError:
            flash('Invalid date format. Use YYYY-MM-DD.', 'danger')
            return render_template('register.html')

        # Create new user
        user = User(username=username, full_name=full_name, qualification=qualification, dob=dob)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.index'))
