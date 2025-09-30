from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from datetime import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum('admin', 'coordinator', 'field_officer'), nullable=False)
    area_code = db.Column(db.String(20), db.ForeignKey('areas.code'))
    active = db.Column(db.Boolean, default=True)
    imei = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    
    # Relationships
    area = db.relationship('Area', backref='users')
    officer = db.relationship('Officer', uselist=False, backref='user', foreign_keys='Officer.user_id')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_id(self):
        return str(self.id)

class Area(db.Model):
    __tablename__ = 'areas'
    
    code = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'<Area {self.name}>'

class Officer(db.Model):
    __tablename__ = 'officers'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    rbm_code = db.Column(db.String(20))
    coordinator_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    active = db.Column(db.Boolean, default=True)
    imei = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    coordinator = db.relationship('User', foreign_keys=[coordinator_id])
    
    def __repr__(self):
        return f'<Officer {self.id}>'

class Transaction(db.Model):
    __tablename__ = 'transactions'
    
    id = db.Column(db.Integer, primary_key=True)
    idpel = db.Column(db.String(20), nullable=False)
    periode = db.Column(db.Date, nullable=False)
    total = db.Column(db.Numeric(10, 2), nullable=False)
    payment_type = db.Column(db.Enum('cash', 'installment', 'transfer'), default='cash')
    officer_id = db.Column(db.Integer, db.ForeignKey('officers.id'), nullable=False)
    status = db.Column(db.Enum('pending', 'completed', 'failed'), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship
    officer = db.relationship('Officer', backref='transactions')
    
    def __repr__(self):
        return f'<Transaction {self.id}>'

class TalanganTransaction(db.Model):
    __tablename__ = 'talangan_transactions'
    
    id = db.Column(db.Integer, primary_key=True)
    idpel = db.Column(db.String(20), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Enum('pending', 'approved', 'rejected', 'settled'), default='pending')
    officer_id = db.Column(db.Integer, db.ForeignKey('officers.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship
    officer = db.relationship('Officer', backref='talangan_transactions')
    
    def __repr__(self):
        return f'<TalanganTransaction {self.id}>'

class WALog(db.Model):
    __tablename__ = 'wa_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    idpel = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text)
    status = db.Column(db.Enum('sent', 'delivered', 'read', 'failed'), default='sent')
    sent_at = db.Column(db.DateTime, default=datetime.utcnow)
    delivered_at = db.Column(db.DateTime)
    read_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<WALog {self.id}>'

class PrintLog(db.Model):
    __tablename__ = 'print_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.Integer, db.ForeignKey('transactions.id'), nullable=False)
    printed_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    file_path = db.Column(db.String(255))
    printed_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    transaction = db.relationship('Transaction', backref='print_logs')
    user = db.relationship('User', backref='print_logs')
    
    def __repr__(self):
        return f'<PrintLog {self.id}>'

class MonitoringLog(db.Model):
    __tablename__ = 'monitoring_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    module_name = db.Column(db.String(100), nullable=False)
    event_type = db.Column(db.String(50), nullable=False)
    details = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship
    user = db.relationship('User', backref='monitoring_logs')
    
    def __repr__(self):
        return f'<MonitoringLog {self.id}>'

class Anomaly(db.Model):
    __tablename__ = 'anomalies'
    
    id = db.Column(db.Integer, primary_key=True)
    idpel = db.Column(db.String(20), nullable=False)
    anomaly_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.Enum('reported', 'investigating', 'resolved'), default='reported')
    reported_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    resolved_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    resolved_at = db.Column(db.DateTime)
    
    # Relationships
    reporter = db.relationship('User', foreign_keys=[reported_by], backref='reported_anomalies')
    resolver = db.relationship('User', foreign_keys=[resolved_by], backref='resolved_anomalies')
    
    def __repr__(self):
        return f'<Anomaly {self.id}>'

class ReportExport(db.Model):
    __tablename__ = 'report_exports'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    report_type = db.Column(db.String(100), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)
    exported_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship
    user = db.relationship('User', backref='report_exports')
    
    def __repr__(self):
        return f'<ReportExport {self.id}>'

class AnomalyMaster(db.Model):
    __tablename__ = 'anomaly_master'
    
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(100))
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<AnomalyMaster {self.code}>'

class DailySettlement(db.Model):
    __tablename__ = 'daily_settlements'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    total_amount = db.Column(db.Numeric(10, 2), nullable=False)
    officer_id = db.Column(db.Integer, db.ForeignKey('officers.id'), nullable=False)
    status = db.Column(db.Enum('pending', 'completed', 'verified'), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    verified_at = db.Column(db.DateTime)
    
    # Relationship
    officer = db.relationship('Officer', backref='daily_settlements')
    
    def __repr__(self):
        return f'<DailySettlement {self.id}>'