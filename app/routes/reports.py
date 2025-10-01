from flask import Blueprint, render_template, request, redirect, url_for, flash, send_file
from flask_login import login_required
from flask_babel import _
from app.models import Transaction, User, Officer, Area, WALog, PrintLog, MonitoringLog, DailySettlement
from app import db
from datetime import datetime, timedelta
from sqlalchemy import func
from app.utils import export_transactions_to_excel, export_to_excel
import decimal

reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/')
@login_required
def index():
    return render_template('reports/index.html')

@reports_bp.route('/rbm')
@login_required
def rbm():
    # Get transaction data grouped by RBM
    rbm_data = db.session.query(
        Officer.rbm_code,
        func.count(Transaction.id).label('count'),
        func.sum(Transaction.total).label('total')
    ).join(Transaction, Officer.id == Transaction.officer_id).group_by(Officer.rbm_code).all()
    
    return render_template('reports/rbm.html', rbm_data=rbm_data)

@reports_bp.route('/coordinator')
@login_required
def coordinator():
    # Get transaction data grouped by coordinator
    coordinator_data = db.session.query(
        User.username,
        func.count(Transaction.id).label('count'),
        func.sum(Transaction.total).label('total')
    ).join(Officer, User.id == Officer.coordinator_id).join(Transaction, Officer.id == Transaction.officer_id).group_by(User.id).all()
    
    return render_template('reports/coordinator.html', coordinator_data=coordinator_data)

@reports_bp.route('/officer')
@login_required
def officer():
    # Get transaction data grouped by officer
    officer_data = db.session.query(
        User.username,
        func.count(Transaction.id).label('count'),
        func.sum(Transaction.total).label('total')
    ).join(Officer, User.id == Officer.user_id).join(Transaction, Officer.id == Transaction.officer_id).group_by(User.id).all()
    
    return render_template('reports/officer.html', officer_data=officer_data)

@reports_bp.route('/area')
@login_required
def area():
    # Get transaction data grouped by area
    area_data = db.session.query(
        Area.name,
        func.count(Transaction.id).label('count'),
        func.sum(Transaction.total).label('total')
    ).join(Officer, Area.code == User.area_code).join(User, Officer.user_id == User.id).join(Transaction, Officer.id == Transaction.officer_id).group_by(Area.code).all()
    
    return render_template('reports/area.html', area_data=area_data)

@reports_bp.route('/tunggakan')
@login_required
def tunggakan():
    # Get outstanding payments (pending transactions)
    tunggakan_data = Transaction.query.filter_by(status='pending').all()
    return render_template('reports/tunggakan.html', tunggakan_data=tunggakan_data)

@reports_bp.route('/wa-monitoring')
@login_required
def wa_monitoring():
    # Get WA logs data
    wa_logs = WALog.query.order_by(WALog.created_at.desc()).all()
    return render_template('reports/wa_monitoring.html', wa_logs=wa_logs)

@reports_bp.route('/log-monitoring')
@login_required
def log_monitoring():
    # Get monitoring logs data
    monitoring_logs = MonitoringLog.query.order_by(MonitoringLog.created_at.desc()).all()
    return render_template('reports/log_monitoring.html', monitoring_logs=monitoring_logs)

@reports_bp.route('/daily-settlement')
@login_required
def daily_settlement():
    # Get daily settlement data
    settlements = DailySettlement.query.order_by(DailySettlement.date.desc()).all()
    return render_template('reports/daily_settlement.html', settlements=settlements)

@reports_bp.route('/bluetooth-print')
@login_required
def bluetooth_print():
    # Get print logs data
    print_logs = PrintLog.query.join(Transaction).order_by(PrintLog.printed_at.desc()).all()
    return render_template('reports/bluetooth_print.html', print_logs=print_logs)

@reports_bp.route('/morning-evening')
@login_required
def morning_evening():
    # This would handle morning-evening settlement monitoring
    # For now, we'll just render the template
    return render_template('reports/morning_evening.html')

@reports_bp.route('/monthly')
@login_required
def monthly():
    # This would handle monthly reports
    # For now, we'll just render the template
    return render_template('reports/monthly.html')

# Export routes
@reports_bp.route('/rbm/export/<format>')
@login_required
def rbm_export(format):
    rbm_data = db.session.query(
        Officer.rbm_code,
        func.count(Transaction.id).label('count'),
        func.sum(Transaction.total).label('total')
    ).join(Transaction, Officer.id == Transaction.officer_id).group_by(Officer.rbm_code).all()
    
    if format == 'excel':
        headers = ['rbm_code', 'count', 'total']
        output, filename = export_to_excel(rbm_data, headers, 'rbm_report')
        return send_file(
            output,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name=filename
        )
    else:
        # For now, only Excel is implemented
        flash('PDF export not yet implemented', 'warning')
        return redirect(url_for('reports.rbm'))

@reports_bp.route('/coordinator/export/<format>')
@login_required
def coordinator_export(format):
    coordinator_data = db.session.query(
        User.username,
        func.count(Transaction.id).label('count'),
        func.sum(Transaction.total).label('total')
    ).join(Officer, User.id == Officer.coordinator_id).join(Transaction, Officer.id == Transaction.officer_id).group_by(User.id).all()
    
    if format == 'excel':
        headers = ['username', 'count', 'total']
        output, filename = export_to_excel(coordinator_data, headers, 'coordinator_report')
        return send_file(
            output,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name=filename
        )
    else:
        # For now, only Excel is implemented
        flash('PDF export not yet implemented', 'warning')
        return redirect(url_for('reports.coordinator'))

@reports_bp.route('/officer/export/<format>')
@login_required
def officer_export(format):
    officer_data = db.session.query(
        User.username,
        func.count(Transaction.id).label('count'),
        func.sum(Transaction.total).label('total')
    ).join(Officer, User.id == Officer.user_id).join(Transaction, Officer.id == Transaction.officer_id).group_by(User.id).all()
    
    if format == 'excel':
        headers = ['username', 'count', 'total']
        output, filename = export_to_excel(officer_data, headers, 'officer_report')
        return send_file(
            output,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name=filename
        )
    else:
        # For now, only Excel is implemented
        flash('PDF export not yet implemented', 'warning')
        return redirect(url_for('reports.officer'))

@reports_bp.route('/tunggakan/export/<format>')
@login_required
def tunggakan_export(format):
    tunggakan_data = Transaction.query.filter_by(status='pending').all()
    
    if format == 'excel':
        output, filename = export_transactions_to_excel(tunggakan_data)
        return send_file(
            output,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name=filename
        )
    else:
        # For now, only Excel is implemented
        flash('PDF export not yet implemented', 'warning')
        return redirect(url_for('reports.tunggakan'))