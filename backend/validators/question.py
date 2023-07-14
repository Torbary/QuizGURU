from flask_wtf import Form
from wtforms import StringField, IntegerField, FieldList
from wtforms.validators import DataRequired, NumberRange, Optional


class QuestionForm(Form):
    """
    QuestionForm:
    represents a form used for validating and processing data related to a quiz question
    """

    question = StringField("Question", validators=[DataRequired()])
    options = FieldList(
        StringField("Option", validators=[DataRequired()]), min_entries=2
    )
    correct = IntegerField(
        "Correct Option", validators=[DataRequired(), NumberRange(min=0)], default=0
    )
    hint = StringField("Hint", validators=[Optional()])
    point = IntegerField("Point", validators=[Optional(), NumberRange(min=1)], default=1)
