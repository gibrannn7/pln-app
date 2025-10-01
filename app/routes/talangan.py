from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from flask_babel import _
from app.models import TalanganTransaction, Officer
from app import db

talangan_bp = Blueprint('talangan', __name__)

@talangan_bp.route('/')
@login_required
def index():
    return render_template('talangan/index.html')

@talangan_bp.route('/balance')
@login_required
def balance():
    # This would implement balance monitoring
    # For now, just render the page
    return render_template('talangan/balance.html')

@talangan_bp.route('/daily-target')
@login_required
def daily_target():
    # This would implement daily target monitoring
    # For now, just render the page
    return render_template('talangan/daily_target.html')

@talangan_bp.route('/transactions')
@login_required
def transactions():
    # Get all talangan transactions
    transactions = TalanganTransaction.query.join(Officer).order_by(TalanganTransaction.date.desc()).all()
    return render_template('talangan/transactions.html', transactions=transactions)

@talangan_bp.route('/detail-payments')
@login_required
def detail_payments():
    # This would handle detail payments (cash/installments)
    # For now, just render the page
    return render_template('talangan/detail_payments.html')

@talangan_bp.route('/input-settlement')
@login_required
def input_settlement():
    # This would handle input settlement
    # For now, just render the page
    return render_template('talangan/input_settlement.html')

@talangan_bp.route('/approval')
@login_required
def approval():
    # This would handle approval process
    # For now, just render the page
    return render_template('talangan/approval.html')

@talangan_bp.route('/photo-downloads')
@login_required
def photo_downloads():
    # This would handle photo downloads
    # For now, just render the page
    return render_template('talangan/photo_downloads.html')