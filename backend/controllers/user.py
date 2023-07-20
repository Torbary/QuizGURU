from models import storage
from models.user import User
from models.quiz import Quiz
from models.score import Score
from sqlalchemy.orm import scoped_session, load_only
from .score import calculate_score


@storage.with_session
def fetch_user_quizzes(session: scoped_session, user_id):
    query = (
        session.query(Quiz)
        .join(User.quizzes)
        .filter(User.id == user_id)
        .options(
            load_only(
                Quiz.id, Quiz.created_at, Quiz.updated_at, Quiz.description, Quiz.title
            )
        )
    )

    quizzes = query.all()
    quizzes = [quiz.to_dict() for quiz in quizzes]
    return quizzes


def add_quiz_to_user(user_id, quiz_id):
    quiz = storage.get(Quiz, quiz_id)
    if not quiz:
        return False

    user: User = storage.get(User, user_id)
    if not user:
        return False

    user.quizzes.append(quiz)
    user.save()
    return True


def update_user_score(user_id, score: Score):
    if not score:
        return False
    user: User = storage.get(User, user_id)
    if not user:
        return False

    # calculate score
    total_score = calculate_score(score)

    if not total_score:
        return False
    score.score = total_score
    score.save()

    user.scores.append(score)
    user.save()

    return True
