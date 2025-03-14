from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from config import Config
from models import db, User
import os

# Import controllers
from controllers.auth import auth_bp
from controllers.admin import admin_bp
from controllers.user import user_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize Flask extensions
    db.init_app(app)
    Bootstrap(app)
    
    # Initialize login manager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(user_bp, url_prefix='/user')
    
    # Create database tables and admin user
    with app.app_context():
        db.create_all()
        create_admin()
    
    return app

def create_admin():
    # Check if admin already exists
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(
            username='admin',
            full_name='Quiz Master Admin',
            is_admin=True
        )
        admin.set_password('admin')
        db.session.add(admin)
        db.session.commit()

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
