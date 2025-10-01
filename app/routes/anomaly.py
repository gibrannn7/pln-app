from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from flask_babel import _
from app.models import Anomaly, AnomalyMaster, User
from app import db

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