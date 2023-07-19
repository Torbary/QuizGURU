from flask_wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange, UUID


class AnswerForm(Form):
    answer = IntegerField(
        "Choice", validators=[DataRequired(), NumberRange(min=0, max=3)]
    )
    question_id = StringField("Question", validators=[DataRequired(), UUID()])
