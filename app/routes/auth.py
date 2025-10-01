import random
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from flask_babel import _
from app.models import User
from app import db

auth_bp = Blueprint('auth', __name__)

def generate_captcha():
    """Generate a simple math captcha"""
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-'])
    
    if operator == '+':
        result = num1 + num2
    else:
        # Ensure the result is positive
        if num1 < num2:
            num1, num2 = num2, num1
        result = num1 - num2
    
    question = f"{num1} {operator} {num2} = ?"
    return question, str(result)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        captcha_answer = request.form['captcha_answer']
        session_captcha = request.form['session_captcha']
        
        # Verify captcha
        if captcha_answer != session_captcha:
            flash(_('Captcha verification failed. Please try again.'), 'error')
            captcha_question, captcha_solution = generate_captcha()
            return render_template('auth/login.html', 
                                 captcha_question=captcha_question, 
                                 session_captcha=captcha_solution)
        
        # Find user in database
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password) and user.active:
            login_user(user)
            user.last_login = db.func.now()
            db.session.commit()
            
            # Redirect based on user role
            if user.role == 'admin':
                return redirect(url_for('dashboard.index'))
            elif user.role == 'coordinator':
                return redirect(url_for('dashboard.index'))
            else:  # field_officer
                return redirect(url_for('dashboard.index'))
        else:
            flash(_('Invalid username or password'), 'error')
    
    # Generate new captcha
    captcha_question, captcha_solution = generate_captcha()
    
    return render_template('auth/login.html', 
                         captcha_question=captcha_question, 
                         session_captcha=captcha_solution)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash(_('You have been logged out.'), 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':
        current_password = request.form['current_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']
        
        # Verify current password
        if not current_user.check_password(current_password):
            flash(_('Current password is incorrect'), 'error')
            return render_template('auth/change_password.html')
        
        # Check if new passwords match
        if new_password != confirm_password:
            flash(_('New passwords do not match'), 'error')
            return render_template('auth/change_password.html')
        
        # Update password
        current_user.set_password(new_password)
        db.session.commit()
        
        flash(_('Password updated successfully'), 'success')
        return redirect(url_for('main.index'))
    
    return render_template('auth/change_password.html')