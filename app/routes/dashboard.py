from flask import Blueprint, render_template
from flask_login import login_required
from app.models import Transaction, User, Officer
from app import db
from datetime import datetime, timedelta
from sqlalchemy import func

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
@login_required
def index():
    # Get summary statistics
    total_transactions = Transaction.query.count()
    completed_transactions = Transaction.query.filter_by(status='completed').count()
    pending_transactions = Transaction.query.filter_by(status='pending').count()
    
    # Get transaction data for the last 6 months for the histogram
    six_months_ago = datetime.now() - timedelta(days=180)
    monthly_data = db.session.query(
        func.date_format(Transaction.periode, '%Y-%m').label('month'),
        func.count(Transaction.id).label('count'),
        func.sum(Transaction.total).label('total')
    ).filter(Transaction.periode >= six_months_ago).group_by('month').all()
    
    # Prepare data for the chart
    months = [row.month for row in monthly_data]
    counts = [row.count for row in monthly_data]
    totals = [float(row.total) if row.total else 0 for row in monthly_data]
    
    # Get recent transactions
    recent_transactions = Transaction.query.order_by(Transaction.created_at.desc()).limit(5).all()
    
    return render_template('dashboard/index.html', 
                          total_transactions=total_transactions,
                          completed_transactions=completed_transactions,
                          pending_transactions=pending_transactions,
                          months=months,
                          counts=counts,
                          totals=totals,
                          recent_transactions=recent_transactions)