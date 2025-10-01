from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from flask_babel import _
from app.models import User, Area, Officer
from app import db
from app.utils import admin_required

master_data_bp = Blueprint('master_data', __name__)

@master_data_bp.route('/')
@login_required
def index():
    return render_template('master_data/index.html')

@master_data_bp.route('/coordinators')
@login_required
@admin_required
def coordinators():
    coordinators = User.query.filter_by(role='coordinator').all()
    return render_template('master_data/coordinators.html', coordinators=coordinators)

@master_data_bp.route('/officers')
@login_required
@admin_required
def officers():
    officers = Officer.query.join(User).all()
    return render_template('master_data/officers.html', officers=officers)

@master_data_bp.route('/officers/toggle/<int:officer_id>', methods=['POST'])
@login_required
@admin_required
def toggle_officer_active(officer_id):
    officer = Officer.query.get_or_404(officer_id)
    officer.active = not officer.active
    db.session.commit()
    status = _('active') if officer.active else _('inactive')
    flash(_('Officer status updated to %(status)s', status=status), 'success')
    return redirect(url_for('master_data.officers'))

@master_data_bp.route('/officers/reset-imei/<int:officer_id>', methods=['POST'])
@login_required
@admin_required
def reset_officer_imei(officer_id):
    officer = Officer.query.get_or_404(officer_id)
    officer.imei = None
    if officer.user:
        officer.user.imei = None
    db.session.commit()
    flash(_('Officer IMEI reset successfully'), 'success')
    return redirect(url_for('master_data.officers'))

@master_data_bp.route('/reset-umt')
@login_required
@admin_required
def reset_umt():
    # This would implement the reset UMT functionality
    # For now, just render the page
    return render_template('master_data/reset_umt.html')
