from flask_wtf import Form, FlaskForm
from wtforms import StringField, IntegerField, FieldList, FormField
from wtforms.validators import DataRequired, Length, Optional, Regexp, NumberRange

from .question import QuestionForm


class QuizForm(Form):
    """
    QuizForm:
    represents a form used for validating and processing data related to a quiz
    """

    title = StringField("Title", validators=[DataRequired(), Length(min=8, max=256)])
    description = StringField("Description", validators=[DataRequired(), Length(min=8)])
    duration = IntegerField(
        "Duration", validators=[Optional(), NumberRange(min=5, max=60)], default=5
    )
    owner_id = StringField(
        "OwnerID",
        validators=[
            Optional(),
            Regexp(regex=r"([a-fA-F0-9]{8})-([a-fA-F0-9]{4}-){3}([a-fA-F0-9]{12})"),
        ],
    )
    questions = FieldList(FormField(QuestionForm))
