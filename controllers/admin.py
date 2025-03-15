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

        quiz = Quiz(chapter_id=chapter_id, date_of_quiz=date_of_quiz, time_duration=time_duration, remarks=remarks)
        db.session.add(quiz)
        db.session.commit()

        flash('Quiz added successfully!', 'success')
        return redirect(url_for('admin.quizzes', chapter_id=chapter_id))

    return render_template('admin/add_quiz.html', chapter=chapter)


@admin_bp.route('/users')
@admin_required
def users():
    users = User.query.filter_by(is_admin=False).all()  # Only show non-admin users
    return render_template('admin/users.html', users=users)


@admin_bp.route('/users/delete/<int:user_id>', methods=['POST'])
@admin_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)

    if user.is_admin:  # Prevent admin deletion
        flash('Cannot delete admin user.', 'danger')
        return redirect(url_for('admin.users'))

    db.session.delete(user)
    db.session.commit()

    flash('User deleted successfully!', 'success')
    return redirect(url_for('admin.users'))


@admin_bp.route('/chapters/<int:subject_id>')
@admin_required
def chapters(subject_id):
    subject = Subject.query.get_or_404(subject_id)
    chapters = Chapter.query.filter_by(subject_id=subject_id).all()

    return render_template('admin/chapters.html', subject=subject, chapters=chapters)


@admin_bp.route('/chapters/add/<int:subject_id>', methods=['GET', 'POST'])
@admin_required
def add_chapter(subject_id):
    subject = Subject.query.get_or_404(subject_id)

    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')

        if not name:
            flash('Chapter name is required.', 'danger')
            return redirect(url_for('admin.add_chapter', subject_id=subject_id))

        chapter = Chapter(name=name, description=description, subject_id=subject_id)
        db.session.add(chapter)
        db.session.commit()

        flash('Chapter added successfully!', 'success')
        return redirect(url_for('admin.chapters', subject_id=subject_id))

    return render_template('admin/add_chapter.html', subject=subject)


@admin_bp.route('/chapters/edit/<int:chapter_id>', methods=['GET', 'POST'])
@admin_required
def edit_chapter(chapter_id):
    chapter = Chapter.query.get_or_404(chapter_id)

    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')

        if not name:
            flash('Chapter name is required.', 'danger')
            return redirect(url_for('admin.edit_chapter', chapter_id=chapter_id))

        chapter.name = name
        chapter.description = description
        db.session.commit()

        flash('Chapter updated successfully!', 'success')
        return redirect(url_for('admin.chapters', subject_id=chapter.subject_id))

    return render_template('admin/edit_chapter.html', chapter=chapter)


@admin_bp.route('/chapters/delete/<int:chapter_id>', methods=['POST'])
@admin_required
def delete_chapter(chapter_id):
    chapter = Chapter.query.get_or_404(chapter_id)
    subject_id = chapter.subject_id  # Store subject ID before deleting

    db.session.delete(chapter)
    db.session.commit()

    flash('Chapter deleted successfully!', 'success')
    return redirect(url_for('admin.chapters', subject_id=subject_id))

@admin_bp.route('/quizzes/<int:chapter_id>')
@admin_required
def quizzes(chapter_id):
    chapter = Chapter.query.get_or_404(chapter_id)
    quizzes = Quiz.query.filter_by(chapter_id=chapter_id).all()

    return render_template('admin/quizzes.html', chapter=chapter, quizzes=quizzes)


@admin_bp.route('/quizzes/edit/<int:quiz_id>', methods=['GET', 'POST'])
@admin_required
def edit_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)

    if request.method == 'POST':
        date_str = request.form.get('date_of_quiz')
        time_duration = request.form.get('time_duration')
        remarks = request.form.get('remarks')

        try:
            date_of_quiz = datetime.strptime(date_str, '%Y-%m-%d').date()
            quiz.date_of_quiz = date_of_quiz
        except ValueError:
            flash('Invalid date format. Use YYYY-MM-DD.', 'danger')
            return redirect(url_for('admin.edit_quiz', quiz_id=quiz_id))

        quiz.time_duration = time_duration
        quiz.remarks = remarks
        db.session.commit()

        flash('Quiz updated successfully!', 'success')
        return redirect(url_for('admin.quizzes', chapter_id=quiz.chapter_id))

    return render_template('admin/edit_quiz.html', quiz=quiz)

@admin_bp.route('/quizzes/delete/<int:quiz_id>', methods=['POST'])
@admin_required
def delete_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    chapter_id = quiz.chapter_id  # Store the chapter ID before deleting the quiz

    db.session.delete(quiz)
    db.session.commit()

    flash('Quiz deleted successfully!', 'success')
    return redirect(url_for('admin.quizzes', chapter_id=chapter_id))

@admin_bp.route('/questions/<int:quiz_id>')
@admin_required
def questions(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = Question.query.filter_by(quiz_id=quiz_id).all()

    return render_template('admin/questions.html', quiz=quiz, questions=questions)

@admin_bp.route('/questions/add/<int:quiz_id>', methods=['GET', 'POST'])
@admin_required
def add_question(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)

    if request.method == 'POST':
        question_statement = request.form.get('question_statement')
        option1 = request.form.get('option1')
        option2 = request.form.get('option2')
        option3 = request.form.get('option3')
        option4 = request.form.get('option4')
        correct_option = request.form.get('correct_option')

        if not all([question_statement, option1, option2, option3, option4, correct_option]):
            flash('All fields are required.', 'danger')
            return redirect(url_for('admin.add_question', quiz_id=quiz_id))

        question = Question(
            quiz_id=quiz_id,
            question_statement=question_statement,
            option1=option1,
            option2=option2,
            option3=option3,
            option4=option4,
            correct_option=int(correct_option)
        )

        db.session.add(question)
        db.session.commit()

        flash('Question added successfully!', 'success')
        return redirect(url_for('admin.questions', quiz_id=quiz_id))

    return render_template('admin/add_question.html', quiz=quiz)


@admin_bp.route('/questions/edit/<int:question_id>', methods=['GET', 'POST'])
@admin_required
def edit_question(question_id):
    question = Question.query.get_or_404(question_id)

    if request.method == 'POST':
        question_statement = request.form.get('question_statement')
        option1 = request.form.get('option1')
        option2 = request.form.get('option2')
        option3 = request.form.get('option3')
        option4 = request.form.get('option4')
        correct_option = request.form.get('correct_option')

        if not all([question_statement, option1, option2, option3, option4, correct_option]):
            flash('All fields are required.', 'danger')
            return redirect(url_for('admin.edit_question', question_id=question_id))

        question.question_statement = question_statement
        question.option1 = option1
        question.option2 = option2
        question.option3 = option3
        question.option4 = option4
        question.correct_option = int(correct_option)

        db.session.commit()

        flash('Question updated successfully!', 'success')
        return redirect(url_for('admin.questions', quiz_id=question.quiz_id))

    return render_template('admin/edit_question.html', question=question)

@admin_bp.route('/questions/delete/<int:question_id>', methods=['POST'])
@admin_required
def delete_question(question_id):
    question = Question.query.get_or_404(question_id)
    quiz_id = question.quiz_id  # Store quiz ID before deleting

    db.session.delete(question)
    db.session.commit()

    flash('Question deleted successfully!', 'success')
    return redirect(url_for('admin.questions', quiz_id=quiz_id))
