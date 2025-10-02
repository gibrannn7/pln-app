from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from flask_babel import _
from app.models import Anomaly, AnomalyMaster, User
from app import db
from datetime import datetime

anomaly_bp = Blueprint('anomaly', __name__)

@anomaly_bp.route('/')
@login_required
def index():
    return render_template('anomaly/index.html')

@anomaly_bp.route('/daily-reports')
@login_required
def daily_reports():
    anomalies = Anomaly.query.order_by(Anomaly.created_at.desc()).all()
    return render_template('anomaly/daily_reports.html', anomalies=anomalies)

@anomaly_bp.route('/daily-reports/add', methods=['GET', 'POST'])
@login_required
def add_anomaly():
    if request.method == 'POST':
        idpel = request.form.get('idpel')
        anomaly_type = request.form.get('anomaly_type')
        description = request.form.get('description')
        
        anomaly = Anomaly(
            idpel=idpel,
            anomaly_type=anomaly_type,
            description=description,
            reported_by=current_user.id,
            status='reported'
        )
        db.session.add(anomaly)
        db.session.commit()
        flash(_('Anomaly report added successfully'), 'success')
        return redirect(url_for('anomaly.daily_reports'))
    
    return render_template('anomaly/add_anomaly.html')

@anomaly_bp.route('/daily-reports/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_anomaly(id):
    anomaly = Anomaly.query.get_or_404(id)
    
    if request.method == 'POST':
        anomaly.idpel = request.form.get('idpel')
        anomaly.anomaly_type = request.form.get('anomaly_type')
        anomaly.description = request.form.get('description')
        anomaly.status = request.form.get('status', 'reported')
        
        if anomaly.status == 'resolved':
            anomaly.resolved_by = current_user.id
            anomaly.resolved_at = datetime.utcnow()
        
        db.session.commit()
        flash(_('Anomaly report updated successfully'), 'success')
        return redirect(url_for('anomaly.daily_reports'))
    
    return render_template('anomaly/edit_anomaly.html', anomaly=anomaly)

@anomaly_bp.route('/daily-reports/delete/<int:id>', methods=['POST'])
@login_required
def delete_anomaly(id):
    anomaly = Anomaly.query.get_or_404(id)
    db.session.delete(anomaly)
    db.session.commit()
    flash(_('Anomaly report deleted successfully'), 'success')
    return redirect(url_for('anomaly.daily_reports'))

@anomaly_bp.route('/daily-reports/resolve/<int:id>', methods=['POST'])
@login_required
def resolve_anomaly(id):
    anomaly = Anomaly.query.get_or_404(id)
    anomaly.status = 'resolved'
    anomaly.resolved_by = current_user.id
    anomaly.resolved_at = datetime.utcnow()
    db.session.commit()
    flash(_('Anomaly report resolved successfully'), 'success')
    return redirect(url_for('anomaly.daily_reports'))

@anomaly_bp.route('/recap-officer')
@login_required
def recap_officer():
    # This would implement recap per officer
    # For now, just render the page
    return render_template('anomaly/recap_officer.html')

@anomaly_bp.route('/recap-date')
@login_required
def recap_date():
    # This would implement recap per date
    # For now, just render the page
    return render_template('anomaly/recap_date.html')

@anomaly_bp.route('/master-data')
@login_required
def master_data():
    anomaly_masters = AnomalyMaster.query.all()
    return render_template('anomaly/master_data.html', anomaly_masters=anomaly_masters)

@anomaly_bp.route('/master-data/add', methods=['GET', 'POST'])
@login_required
def add_anomaly_master():
    if request.method == 'POST':
        code = request.form.get('code')
        description = request.form.get('description')
        category = request.form.get('category')
        active = request.form.get('active') == 'on'
        
        anomaly_master = AnomalyMaster(
            code=code,
            description=description,
            category=category,
            active=active
        )
        db.session.add(anomaly_master)
        db.session.commit()
        flash(_('Anomaly master data added successfully'), 'success')
        return redirect(url_for('anomaly.master_data'))
    
    return render_template('anomaly/add_anomaly_master.html')

@anomaly_bp.route('/master-data/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_anomaly_master(id):
    anomaly_master = AnomalyMaster.query.get_or_404(id)
    
    if request.method == 'POST':
        anomaly_master.code = request.form.get('code')
        anomaly_master.description = request.form.get('description')
        anomaly_master.category = request.form.get('category')
        anomaly_master.active = request.form.get('active') == 'on'
        
        db.session.commit()
        flash(_('Anomaly master data updated successfully'), 'success')
        return redirect(url_for('anomaly.master_data'))
    
    return render_template('anomaly/edit_anomaly_master.html', anomaly_master=anomaly_master)

@anomaly_bp.route('/master-data/delete/<int:id>', methods=['POST'])
@login_required
def delete_anomaly_master(id):
    anomaly_master = AnomalyMaster.query.get_or_404(id)
    db.session.delete(anomaly_master)
    db.session.commit()
    flash(_('Anomaly master data deleted successfully'), 'success')
    return redirect(url_for('anomaly.master_data'))