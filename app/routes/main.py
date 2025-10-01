from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_login import login_required
from flask_babel import _
from app.utils import admin_required, coordinator_required, field_officer_required

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def index():
    # Redirect to dashboard based on user role
    return redirect(url_for('dashboard.index'))

@main_bp.route('/profile')
@login_required
def profile():
    return render_template('main/profile.html')

@main_bp.route('/language/<lang_code>')
def set_language(lang_code):
    # Set the language in session
    session['language'] = lang_code
    # Flash message to confirm language change
    if lang_code == 'id':
        flash(_('Bahasa diubah menjadi Indonesia'), 'info')
    else:
        flash(_('Language changed to English'), 'info')
    # Redirect back to the previous page
    from flask import request
    return redirect(request.referrer or url_for('dashboard.index'))

# Error handlers
@main_bp.app_errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html'), 403

@main_bp.app_errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404

@main_bp.app_errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500