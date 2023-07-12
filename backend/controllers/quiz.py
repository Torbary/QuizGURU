#!/usr/bin/python3

"""
Quiz Controller method.
"""
from models import storage
from models.quiz import Quiz
from controllers.question import get_question
from sqlalchemy.orm import scoped_session, load_only


@storage.with_session
def get_quiz(session: scoped_session, id):
    """
    fetch and properly format the quiz data.
    """
    quiz : Quiz = storage.get(Quiz, id)
    if not quiz:
        return None
    data = {
        "questions": []
    }
    keys = ('title', 'description', 'updated_at',
            'created_at', 'id', 'duration')
    for k, v in quiz.__dict__.items():
        if k in keys:
            data.update({k: v})
    for question in quiz.questions:
        question = get_question(question.id)
        data["questions"].append(question)
    if "duration" not in data.keys():
        # 5 minutes
        data["duration"] = 10 * 60 * 1000
    return data

@storage.with_session
def fetch_quizzes(session: scoped_session, page_size = 50, page_no = 1, full_fetch=False):
    """
    retrieves the quizzes based on a specified pagination
    page size can be 25, 50, 100
    """
    if page_size not in (25, 50, 100):
        page_size = 50
    if page_no <= 0:
        page_no = 1
    offset = (page_no - 1) * page_size
    query = session.query(Quiz)\
        .order_by(Quiz.id, Quiz.created_at)\
        .limit(page_size)\
        .offset(offset)
    if not full_fetch:
        query = query.options(load_only(Quiz.id, Quiz.created_at,
                            Quiz.updated_at, Quiz.description, Quiz.title))
    return query.all()

