import os

class Config:
    # Secret key for session management and CSRF protection
    SECRET_KEY = 'your-secret-key-goes-here'
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///quiz_master.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Upload path for any static files
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/uploads')
