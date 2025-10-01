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
        idpel = request.form.get('idpel')
        # Find transactions for this customer
        transactions = Transaction.query.filter_by(idpel=idpel).all()
        if transactions:
            # Get user info from the first transaction
            transaction = transactions[0]
            customer_data = {
                'idpel': idpel,
                'transactions': transactions,
                'officer_name': transaction.officer.user.username if transaction.officer.user else 'N/A'
            }
    
    return render_template('information/customer_lookup.html', customer_data=customer_data)