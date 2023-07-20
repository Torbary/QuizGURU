from models.answer import Answer
from models.score import Score
from validators.answer import AnswerForm
from models import storage
from sqlalchemy import and_
from sqlalchemy.orm import scoped_session


@storage.with_session
def create_answer(session: scoped_session, data, quiz_id, score_id):
    """
    controller function that creates an answer
    and return it.
    """
    form: AnswerForm = AnswerForm(data=data)
    if not form.validate():
        return None
    question_id = data["question_id"]
    # ensure the answer model does not exist before
    exist = (
        session.query(Answer)
        .filter(
            and_(
                Answer.score_id == score_id,
                Answer.quiz_id == quiz_id,
                Answer.question_id == question_id,
            )
        )
        .first()
    )
    # return it if it does.
    if exist:
        return exist
    answer = Answer(**data)
    answer.quiz_id = quiz_id
    answer.score_id = score_id
    answer.save()
    return answer
