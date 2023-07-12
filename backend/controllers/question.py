from models import storage
from models.question import Question
from sqlalchemy.orm import scoped_session, load_only


@storage.with_session
def get_question(session: scoped_session, id):
    data = {}
    keys = (
        "id", "question",
        "options", "quiz_id",
    )
    question = session.query(Question) \
        .options(load_only(
            Question.id, Question.question, Question.options,
            Question.quiz_id
        )) \
        .filter_by(id=id) \
        .first()
    
    for k,v in question.__dict__.items():
        if k in keys:
            data.update({k: v})
    
    return data
