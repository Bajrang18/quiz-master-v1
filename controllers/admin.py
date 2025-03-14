from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models import db, User, Subject, Chapter, Quiz, Question
from datetime import datetime

admin_bp = Blueprint('admin', __name__)

def admin_required(func):
    def wrapper(*args, **kwargs):
        if not current_user.is_admin:
            flash('Admin access required', 'danger')
            return redirect(url_for('auth.index'))
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return login_required(wrapper)

@admin_bp.route('/dashboard')
@admin_required
def dashboard():
    return render_template('admin/dashboard.html')

@admin_bp.route('/subjects', methods=['GET', 'POST'])
@admin_required
def subjects():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        
        if not name:
            flash('Subject name is required', 'danger')
            return redirect(url_for('admin.subjects'))
        
        subject = Subject(name=name, description=description)
        db.session.add(subject)
        db.session.commit()
        flash('Subject added successfully!', 'success')
    
    subjects = Subject.query.all()
    return render_template('admin/subjects.html', subjects=subjects)

@admin_bp.route('/subjects/delete/<int:subject_id>', methods=['POST'])
@admin_required
def delete_subject(subject_id):
    subject = Subject.query.get_or_404(subject_id)
    db.session.delete(subject)
    db.session.commit()
    
    flash('Subject deleted successfully', 'success')
    return redirect(url_for('admin.subjects'))


@admin_bp.route('/subjects/add', methods=['GET', 'POST'])
@admin_required
def add_subject():
    if request.method == 'POST':
        name = request.form.get('name').strip()
        description = request.form.get('description').strip()

        if not name:
            flash('Subject name is required.', 'danger')
            return redirect(url_for('admin.add_subject'))

        # Prevent duplicate subjects
        if Subject.query.filter_by(name=name).first():
            flash('Subject already exists.', 'danger')
            return redirect(url_for('admin.add_subject'))

        subject = Subject(name=name, description=description)
        db.session.add(subject)
        db.session.commit()

        flash('Subject added successfully!', 'success')
        return redirect(url_for('admin.subjects'))

    return render_template('admin/add_subject.html')

@admin_bp.route('/quizzes/add/<int:chapter_id>', methods=['GET', 'POST'])
@admin_required
def add_quiz(chapter_id):
    chapter = Chapter.query.get_or_404(chapter_id)

    if request.method == 'POST':
        date_str = request.form.get('date_of_quiz')
        time_duration = request.form.get('time_duration')
        remarks = request.form.get('remarks', '').strip()

        if not date_str or not time_duration:
            flash('Date and duration are required.', 'danger')
            return redirect(url_for('admin.add_quiz', chapter_id=chapter_id))

        try:
            date_of_quiz = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            flash('Invalid date format. Use YYYY-MM-DD.', 'danger')
            return redirect(url_for('admin.add_quiz', chapter_id=chapter_id))

        # Prevent duplicate quizzes on the same date for the chapter
        if Quiz.query.filter_by(chapter_id=chapter_id, date_of_quiz=date_of_quiz).first():
            flash('A quiz already exists for this chapter on this date.', 'danger')
            return redirect(url_for('admin.add_quiz', chapter_id=chapter_id))

        quiz = Quiz(chapter_id=chapter_id, date_of_quiz=date_of_quiz, time_duration=time_duration, remarks=remarks)
        db.session.add(quiz)
        db.session.commit()

        flash('Quiz added successfully!', 'success')
        return redirect(url_for('admin.quizzes', chapter_id=chapter_id))

    return render_template('admin/add_quiz.html', chapter=chapter)
