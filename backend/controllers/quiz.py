#!/usr/bin/python3

"""
Quiz Controller method.
"""
from models import storage
from models.quiz import Quiz
from controllers.question import fetch_questions, post_questions
from sqlalchemy.orm import scoped_session, load_only


def get_quiz(id):
    """
    fetch and properly format the quiz data.
    """
    quiz : Quiz = storage.get(Quiz, id)
    if not quiz:
        return None
    result = quiz.to_dict()
    
    result["questions"] = fetch_questions(quiz.id)
    if "duration" not in result.keys():
        # 5 minutes
        result["duration"] = 10 * 60 * 1000
    return result

@storage.with_session
def fetch_quizzes(session: scoped_session, page_size = 50, page_no = 1):
    """
    retrieves the quizzes based on a specified pagination
    page size can be 25, 50, 100
    """
    try:
        page_size = int(page_size)
        page_no = int(page_no)
    except ValueError as e:
        return e.__str__()
    if page_size not in (25, 50, 100):
        page_size = 25
        page_no = 1
    elif page_no <= 0:
        page_no = 1
    offset = (page_no - 1) * page_size
    query = session.query(Quiz)\
        .order_by(Quiz.id, Quiz.created_at)\
        .limit(page_size)\
        .offset(offset)
    query = query.options(load_only(Quiz.id, Quiz.created_at,
                        Quiz.updated_at, Quiz.description, Quiz.title))
    result = query.all()
    result = [model.to_dict() for model in result]
    return result

def post_quiz(data: dict):
    """
    handler for quiz creation.
    """
    
    data.pop("id", None)
    data.pop("created_at", None)
    data.pop("updated_at", None)

    questions = data.pop('questions')
    quiz = Quiz(**data)
    quiz.save()

    cond = post_questions(questions, quiz.id)
    if not cond:
        storage.delete(quiz.id)
        storage.save()
        return False
    else:
        return True

