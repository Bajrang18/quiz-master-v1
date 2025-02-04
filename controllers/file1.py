from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class User(db.model):
    id = db.Column(db.String(120), primary_key=True)