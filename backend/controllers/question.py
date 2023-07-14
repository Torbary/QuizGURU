from models.quiz import Quiz
from models import storage
from models.question import Question
from sqlalchemy.orm import scoped_session, load_only


@storage.with_session
def get_question(session: scoped_session, id):
    """
    method to fetch a question based on it id.
    """
    result = session.query(Question) \
        .options(load_only(
            Question.id, Question.question, Question.options,
            Question.quiz_id
        )) \
        .filter_by(id=id) \
        .first()

    return result.to_dict()

@storage.with_session
def fetch_questions(session: scoped_session, quiz_id):
    """
    method to fetch questions of a quiz.
    """
    result = session.query(Question) \
        .options(load_only(
            Question.id, Question.question, Question.options,
            Question.quiz_id
        )) \
        .filter_by(quiz_id=quiz_id) \
        .all()
    
    result = [model.to_dict() for model in result]
    return result

def post_question(data: dict, quiz_id):
    """
    helper function that handles the creation of a question model.
    """
    keys = data.keys()
    required_keys = ("question", "options", "correct")

    if not all(key in keys for key in required_keys):
        # some required fields are missing.
        print("some required fields are missing.")
        return None
    
    data.pop("id", None)
    data.pop("created_at", None)
    data.pop("updated_at", None)

    if "point" in keys and data['point'] <= 0:
        data.pop("point")

    if storage.get(Quiz, quiz_id) is None:
        # the provided quiz id does not exists.
        print("the provided quiz id does not exists.")
        return None
    model = Question(**data)
    model.quiz_id = quiz_id

    return model

def post_questions(questions: list, quiz_id):
    """
    handler that creates multiple question models
    """
    models : list[Question] = []

    for question in questions:
        output = post_question(question, quiz_id)
        if output is None:
            return False
        else:
            models.append(output)
    
    for model in models:
        model.save()
    return True
