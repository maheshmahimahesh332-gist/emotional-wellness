import json
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import MindfulnessExercise, ExerciseCompletion, MoodEntry
from datetime import datetime, timedelta

mindfulness_bp = Blueprint('mindfulness', __name__)

MOOD_TO_CATEGORIES = {
    'anxious': ['breathing', 'meditation'],
    'stressed': ['breathing', 'body_scan'],
    'sad': ['meditation', 'body_scan'],
    'angry': ['breathing', 'meditation'],
    'neutral': ['breathing', 'meditation', 'body_scan'],
    'calm': ['meditation', 'body_scan'],
    'happy': ['meditation', 'body_scan']
}


@mindfulness_bp.route('/')
@login_required
def index():
    exercises = MindfulnessExercise.query.all()

    # Group by category
    categories = {}
    for exercise in exercises:
        if exercise.category not in categories:
            categories[exercise.category] = []
        categories[exercise.category].append(exercise)

    # Get recommendations
    recommendations = get_recommendations()

    completions = ExerciseCompletion.query.filter_by(user_id=current_user.id)\
        .order_by(ExerciseCompletion.completed_at.desc()).limit(10).all()

    return render_template('mindfulness/index.html',
                           categories=categories,
                           recommendations=recommendations,
                           completions=completions)


@mindfulness_bp.route('/exercise/<int:exercise_id>')
@login_required
def exercise(exercise_id):
    ex = MindfulnessExercise.query.get_or_404(exercise_id)
    steps = json.loads(ex.steps)
    return render_template('mindfulness/exercise.html', exercise=ex, steps=steps)


@mindfulness_bp.route('/complete/<int:exercise_id>', methods=['POST'])
@login_required
def complete(exercise_id):
    ex = MindfulnessExercise.query.get_or_404(exercise_id)

    completion = ExerciseCompletion(
        user_id=current_user.id,
        exercise_id=exercise_id
    )
    db.session.add(completion)
    db.session.commit()

    flash(f'Great job completing "{ex.title}"! Would you like to log your mood?', 'success')
    return redirect(url_for('mood.log'))


def get_recommendations():
    """Get exercise recommendations based on user's mood and history."""
    # Get most recent mood
    latest_mood = MoodEntry.query.filter_by(user_id=current_user.id)\
        .order_by(MoodEntry.created_at.desc()).first()

    # Get completed exercises in last 30 days
    month_ago = datetime.utcnow() - timedelta(days=30)
    recent_completions = ExerciseCompletion.query.filter(
        ExerciseCompletion.user_id == current_user.id,
        ExerciseCompletion.completed_at >= month_ago
    ).all()

    if not latest_mood and not recent_completions:
        # No history - suggest beginner exercises
        return MindfulnessExercise.query.filter_by(difficulty='beginner').limit(3).all()

    # Determine recommended categories based on mood
    if latest_mood:
        categories = MOOD_TO_CATEGORIES.get(latest_mood.mood, ['breathing', 'meditation', 'body_scan'])
    else:
        categories = ['breathing', 'meditation', 'body_scan']

    # Determine appropriate difficulty
    if recent_completions:
        completed_difficulties = set(c.exercise.difficulty for c in recent_completions if c.exercise)
        if 'advanced' in completed_difficulties:
            difficulties = ['intermediate', 'advanced']
        elif 'intermediate' in completed_difficulties:
            difficulties = ['beginner', 'intermediate', 'advanced']
        else:
            difficulties = ['beginner', 'intermediate']
    else:
        difficulties = ['beginner']

    # Query matching exercises
    recommendations = MindfulnessExercise.query.filter(
        MindfulnessExercise.category.in_(categories),
        MindfulnessExercise.difficulty.in_(difficulties)
    ).limit(3).all()

    if not recommendations:
        recommendations = MindfulnessExercise.query.filter_by(difficulty='beginner').limit(3).all()

    return recommendations