from app import app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    full_name = db.Column(db.String(150), nullable=False)
    qualification = db.Column(db.String(150), nullable=True)
    dob = db.Column(db.String(150), nullable=True)

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.id'), nullable=False)
    date_of_quiz = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.String(10), nullable=False)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    option1 = db.Column(db.String(150), nullable=False)
    option2 = db.Column(db.String(150), nullable=False)
    option3 = db.Column(db.String(150), nullable=False)
    option4 = db.Column(db.String(150), nullable=False)
    correct_option = db.Column(db.Integer, nullable=False)

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)

# with app.app_context():
#     db.create_all()
#     # if admin exists, else create admin
#     admin = User.query.filter_by(is_admin=True).first()
#     if not admin:
#         password_hash = generate_password_hash('admin')
#         admin = User(username='admin', passhash=password_hash, name='Admin', is_admin=True)
#         db.session.add(admin)
#         db.session.commit()
