from flask_wtf import Form
from .answer import AnswerForm
from wtforms import StringField, IntegerField, FormField, FieldList
from wtforms.validators import DataRequired, UUID


class ScoreForm(Form):
    answers = FieldList(FormField(AnswerForm))
    quiz_id = StringField("Quiz", validators=[DataRequired(), UUID()])
