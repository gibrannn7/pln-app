import pandas as pd
from io import BytesIO
import decimal
from functools import wraps
from flask import abort, send_file
from flask_login import current_user
from datetime import datetime
from app.models import Transaction, User, Officer, Area, TalanganTransaction, Anomaly

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

def coordinator_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role not in ['admin', 'coordinator']:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

def field_officer_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role not in ['admin', 'coordinator', 'field_officer']:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

def role_required(allowed_roles):
    """Decorator to require specific roles"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated or current_user.role not in allowed_roles:
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def export_to_excel(query_result, headers, filename_prefix):
    """Generic function to export query results to Excel"""
    # Convert query result to list of dictionaries
    data = []
    for row in query_result:
        row_dict = {}
        for header in headers:
            # Handle different object types
            if hasattr(row, header):
                value = getattr(row, header)
            elif isinstance(row, (list, tuple)):
                # Handle tuple results from aggregate queries
                if headers.index(header) < len(row):
                    value = row[headers.index(header)]
                else:
                    value = None
            else:
                value = None
                
            # Format dates and decimals appropriately
            if isinstance(value, datetime):
                value = value.strftime('%Y-%m-%d %H:%M:%S')
            elif hasattr(value, 'strftime'):  # Other datetime objects
                value = value.strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(value, decimal.Decimal):
                value = float(value)
                
            row_dict[header] = value
        data.append(row_dict)
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=headers)
    
    # Create Excel file in memory
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    
    output.seek(0)
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{filename_prefix}_{timestamp}.xlsx"
    
    return output, filename

def export_transactions_to_excel(transactions):
    """Export transactions to Excel"""
    headers = ['id', 'idpel', 'periode', 'total', 'payment_type', 'status', 'officer_name', 'created_at']
    
    # Prepare data with officer name
    processed_transactions = []
    for t in transactions:
        processed_t = {
            'id': t.id,
            'idpel': t.idpel,
            'periode': t.periode,
            'total': float(t.total) if t.total else 0,
            'payment_type': t.payment_type,
            'status': t.status,
            'officer_name': t.officer.user.username if t.officer and t.officer.user else 'N/A',
            'created_at': t.created_at
        }
        processed_transactions.append(processed_t)
    
    return export_to_excel(processed_transactions, headers, 'transactions')