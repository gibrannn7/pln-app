from app import create_app
from app.models import db
from app import models  # Import models for Flask-Migrate

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': models.User, 'Transaction': models.Transaction}

if __name__ == '__main__':
    app.run(debug=True)