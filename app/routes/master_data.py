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
    area_code = request.args.get('area', '')
    
    query = User.query.filter_by(role='coordinator')
    if area_code:
        query = query.filter(User.area_code == area_code)
    
    coordinators = query.all()
    
    # Get all areas for the filter dropdown
    areas = Area.query.all()
    
    return render_template('master_data/coordinators.html', coordinators=coordinators, areas=areas, selected_area=area_code)

@master_data_bp.route('/coordinators/add', methods=['GET', 'POST'])
@login_required
@admin_required
def add_coordinator():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        area_code = request.form.get('area_code')
        
        # Check if username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash(_('Username already exists'), 'error')
            return redirect(url_for('master_data.coordinators'))
        
        # Create new coordinator
        coordinator = User(
            username=username,
            role='coordinator',
            area_code=area_code
        )
        coordinator.set_password(password)
        
        db.session.add(coordinator)
        db.session.commit()
        flash(_('Coordinator added successfully'), 'success')
        return redirect(url_for('master_data.coordinators'))
    
    areas = Area.query.all()
    return render_template('master_data/add_coordinator.html', areas=areas)

@master_data_bp.route('/coordinators/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_coordinator(id):
    coordinator = User.query.get_or_404(id)
    
    if request.method == 'POST':
        username = request.form.get('username')
        new_password = request.form.get('password')
        area_code = request.form.get('area_code')
        
        # Check if username already exists (excluding current user)
        existing_user = User.query.filter(User.username == username, User.id != id).first()
        if existing_user:
            flash(_('Username already exists'), 'error')
            return redirect(url_for('master_data.edit_coordinator', id=id))
        
        coordinator.username = username
        coordinator.area_code = area_code
        
        if new_password:  # Only update password if provided
            coordinator.set_password(new_password)
        
        db.session.commit()
        flash(_('Coordinator updated successfully'), 'success')
        return redirect(url_for('master_data.coordinators'))
    
    areas = Area.query.all()
    return render_template('master_data/edit_coordinator.html', coordinator=coordinator, areas=areas)

@master_data_bp.route('/coordinators/delete/<int:id>', methods=['POST'])
@login_required
@admin_required
def delete_coordinator(id):
    coordinator = User.query.get_or_404(id)
    
    # Prevent deletion of current user
    if coordinator.id == current_user.id:
        flash(_('You cannot delete yourself'), 'error')
        return redirect(url_for('master_data.coordinators'))
    
    # Check if coordinator has related officers
    # This requires checking if any officers are assigned to this coordinator
    officers = Officer.query.filter_by(coordinator_id=coordinator.id).all()
    if officers:
        flash(_('Cannot delete coordinator with assigned officers'), 'error')
        return redirect(url_for('master_data.coordinators'))
    
    db.session.delete(coordinator)
    db.session.commit()
    flash(_('Coordinator deleted successfully'), 'success')
    return redirect(url_for('master_data.coordinators'))

@master_data_bp.route('/officers')
@login_required
@admin_required
def officers():
    officers = Officer.query.join(User, Officer.user_id == User.id).all()
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

@master_data_bp.route('/reset-umt', methods=['GET', 'POST'])
@login_required
@admin_required
def reset_umt():
    if request.method == 'POST':
        # Process the reset options here
        reset_users = request.form.getlist('reset_users')
        reset_transactions = request.form.getlist('reset_transactions')
        reset_talangan = request.form.getlist('reset_talangan')
        
        # Perform the reset operations based on selected options
        reset_messages = []
        
        if reset_users:
            # Reset user data
            User.query.update({User.imei: None})
            reset_messages.append("User IMEI data has been reset")
        
        if reset_transactions:
            # Reset transaction data
            Transaction.query.delete()
            reset_messages.append("Transaction data has been cleared")
        
        if reset_talangan:
            # Reset talangan transaction data
            TalanganTransaction.query.delete()
            reset_messages.append("Talangan transaction data has been cleared")
        
        db.session.commit()
        
        if reset_messages:
            for msg in reset_messages:
                flash(_(msg), 'success')
        else:
            flash(_('No reset options were selected'), 'info')
        
        return redirect(url_for('master_data.reset_umt'))
    
    return render_template('master_data/reset_umt.html')
