from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from flask_babel import _
from app.models import TalanganTransaction, Officer, User
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

@talangan_bp.route('/transactions/add', methods=['GET', 'POST'])
@login_required
def add_transaction():
    if request.method == 'POST':
        idpel = request.form.get('idpel')
        amount = request.form.get('amount')
        date = request.form.get('date')
        officer_id = request.form.get('officer_id')
        
        # Create new transaction
        transaction = TalanganTransaction(
            idpel=idpel,
            amount=amount,
            date=date,
            officer_id=officer_id
        )
        db.session.add(transaction)
        db.session.commit()
        flash(_('Talangan transaction added successfully'), 'success')
        return redirect(url_for('talangan.transactions'))
    
    officers = Officer.query.join(User, Officer.user_id == User.id).all()
    return render_template('talangan/add_transaction.html', officers=officers)

@talangan_bp.route('/transactions/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_transaction(id):
    transaction = TalanganTransaction.query.get_or_404(id)
    
    if request.method == 'POST':
        transaction.idpel = request.form.get('idpel')
        transaction.amount = request.form.get('amount')
        transaction.date = request.form.get('date')
        transaction.officer_id = request.form.get('officer_id')
        transaction.status = request.form.get('status', 'pending')
        
        db.session.commit()
        flash(_('Talangan transaction updated successfully'), 'success')
        return redirect(url_for('talangan.transactions'))
    
    officers = Officer.query.join(User, Officer.user_id == User.id).all()
    return render_template('talangan/edit_transaction.html', transaction=transaction, officers=officers)

@talangan_bp.route('/transactions/delete/<int:id>', methods=['POST'])
@login_required
def delete_transaction(id):
    transaction = TalanganTransaction.query.get_or_404(id)
    db.session.delete(transaction)
    db.session.commit()
    flash(_('Talangan transaction deleted successfully'), 'success')
    return redirect(url_for('talangan.transactions'))

@talangan_bp.route('/detail-payments')
@login_required
def detail_payments():
    # This would handle detail payments (cash/installments)
    # For now, just render the page
    return render_template('talangan/detail_payments.html')

@talangan_bp.route('/input-settlement', methods=['GET', 'POST'])
@login_required
def input_settlement():
    if request.method == 'POST':
        # Handle form submission
        pass

    officers = Officer.query.join(User, Officer.user_id == User.id).all()
    return render_template('talangan/input_settlement.html', officers=officers)

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