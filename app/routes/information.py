from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from flask_babel import _
from app.models import User, Transaction
from app import db

information_bp = Blueprint('information', __name__)

@information_bp.route('/')
@login_required
def index():
    return render_template('information/index.html')

@information_bp.route('/customer-lookup', methods=['GET', 'POST'])
@login_required
def customer_lookup():
    customer_data = None
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        
        # Search by idpel or other customer information
        # First, try direct ID Pelanggan match
        transactions = Transaction.query.filter_by(idpel=search_query).all()
        
        if not transactions:
            # If no transactions found by idpel, try searching in other related tables
            # Look for customer data by name if available in future implementation
            pass
        
        if transactions:
            # Get customer information from the first transaction
            transaction = transactions[0]
            customer_data = {
                'idpel': search_query,
                'transactions': transactions,
                'officer_name': transaction.officer.user.username if transaction.officer.user else 'N/A'
            }
        else:
            flash(_('No customer found with ID: %(id)s', id=search_query), 'warning')
    
    return render_template('information/customer_lookup.html', customer_data=customer_data)