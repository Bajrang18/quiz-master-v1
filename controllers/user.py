from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models import db, Quiz, Score, Question
from datetime import datetime

user_bp = Blueprint('user', __name__)

@user_bp.route('/dashboard')
@login_required
def dashboard():
    quizzes = Quiz.query.all()
    return render_template('user/dashboard.html', quizzes=quizzes)

@user_bp.route('/quiz/<int:quiz_id>', methods=['GET', 'POST'])
@login_required
def attempt_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = Question.query.filter_by(quiz_id=quiz_id).all()

    if request.method == 'POST':
        total_questions = len(questions)
        total_correct = 0

        # Check if the user answered all questions
        for question in questions:
            selected_option = request.form.get(f'question_{question.id}')
            if selected_option is None:
                flash('You must answer all questions!', 'danger')
                return redirect(url_for('user.attempt_quiz', quiz_id=quiz.id))

            if int(selected_option) == question.correct_option:
                total_correct += 1

        # Save the quiz result
        score = Score(quiz_id=quiz.id, user_id=current_user.id, total_scored=total_correct, total_questions=total_questions)
        db.session.add(score)
        db.session.commit()

        flash('Quiz submitted successfully!', 'success')
        return redirect(url_for('user.scores'))

    return render_template('user/quiz_attempt.html', quiz=quiz, questions=questions)

@user_bp.route('/scores')
@login_required
def scores():
    user_scores = Score.query.filter_by(user_id=current_user.id).all()

    # Prepare data for Chart.js
    score_data = [
        {
            "quiz_id": score.quiz_id,
            "total_scored": score.total_scored,
            "total_questions": score.total_questions
        }
        for score in user_scores
    ]

    return render_template('user/quiz_result.html', scores=user_scores, score_data=score_data)
