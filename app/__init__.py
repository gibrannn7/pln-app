import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import pymysql

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = 'psTBpygXXMQqYFtFusLXPFkntPgwACkqlEFjYSQJqQnHXPwApnVmakFNPdPGhCZQ'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/pln_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = 'app/static/uploads'
    
    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'

    # Import User model
    from app.models import User

    # Define user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Import and register blueprints
    from app.routes.auth import auth_bp
    from app.routes.main import main_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.master_data import master_data_bp
    from app.routes.reports import reports_bp
    from app.routes.talangan import talangan_bp
    from app.routes.information import information_bp
    from app.routes.anomaly import anomaly_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    app.register_blueprint(master_data_bp, url_prefix='/master-data')
    app.register_blueprint(reports_bp, url_prefix='/reports')
    app.register_blueprint(talangan_bp, url_prefix='/talangan')
    app.register_blueprint(information_bp, url_prefix='/information')
    app.register_blueprint(anomaly_bp, url_prefix='/anomaly')
    
    # Create upload directory if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    return app