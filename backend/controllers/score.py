from models.quiz import Quiz
from models import storage
from models.score import Score
from models.user import User
from models.question import Question
from validators.score import ScoreForm
from controllers.answer import create_answer
from . import HTTPStatus
from sqlalchemy.orm import scoped_session, load_only
from sqlalchemy import and_


@storage.with_session
def create_score(session: scoped_session, data, user_id):
    """
    this method handles creating scores from the provided data.
    returns:
        message, status code, data: Score | dict | None, boolean
    """
    form: ScoreForm = ScoreForm(data=data)
    # verify if the data matches
    if not form.validate():
        return "form invalidation failed", HTTPStatus.BAD, form.errors, False

    quiz_id = data["quiz_id"]
    print(quiz_id)
    model = (
        session.query(User)
        .join(User.scores)
        .filter(and_(Score.quiz_id == quiz_id, User.id == user_id))
        .first()
    )
    # avoid creating useless score model for the same data.
    if model:
        return ("score already exists for this data", HTTPStatus.CONFLICTS, None, False)
    answers = data["answers"]

    score = Score()
    score.quiz_id = quiz_id
    score.user_id = user_id
    score.save()

    quiz_id = data["quiz_id"]
    for answer in answers:
        model = create_answer(answer, quiz_id, score.id)
        if not model:
            continue
        # avoid duplicates.
        elif model in score.answers:
            continue
        else:
            score.answers.append(model)

    score.save()
    return "success", HTTPStatus.CREATED, score, True


@storage.with_session
def calculate_score(session: scoped_session, score):
    """
    this method calculates the total score for a Score model.
    """
    if not score:
        return None
    answers = score.answers
    questions = session.query(Quiz).filter(Quiz.id == score.quiz_id).first().questions
    total_score = 0
    expected_score = 0
    for question in questions:
        expected_score += question.point
    for answer in answers:
        result = (
            session.query(Question)
            .filter(Question.id == answer.question_id)
            .options(load_only(Question.correct, Question.point))
            .first()
        )

        if not result:
            return None
        if answer.answer == result.correct:
            total_score += result.point

    score_percent = (total_score * 100) / expected_score
    score_percent = round(score_percent)
    return score_percent


@storage.with_session
def get_scores(session: scoped_session, user_id):
    scores = session.query(Score).filter(Score.user_id == user_id).all()

    scores = [score.to_dict() for score in scores]
    return scores


@storage.with_session
def get_score(session: scoped_session, score_id, user_id):
    score = (
        session.query(Score)
        .filter(and_(Score.id == score_id, Score.user_id == user_id))
        .first()
    )
    if not score:
        return None
    answers = score.answers
    data = score.to_dict()
    answers = [answer.to_dict() for answer in answers]
    data["answers"] = answers
    return data
