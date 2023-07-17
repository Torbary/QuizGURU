# from flask_wtf import Form
from wtforms import StringField, Form
from wtforms.validators import DataRequired, Length, Regexp, Email


class UserForm(Form):
    """
    represents a form used for validating and processing data related to a user
    """

    email = StringField("Email", validators=[
        DataRequired(), Email()
    ])
    lastname = StringField("LastName", validators=[
        DataRequired(), Length(min=2, max=128)
    ])
    firstname = StringField("FirstName", validators=[
        DataRequired(), Length(min=2, max=128)
    ])
    password = StringField("Password", validators=[
        DataRequired(), Length(min=8, max=36), Regexp(regex=r'(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s])(?!.*\s).{8,}$')
    ])

class LoginForm(Form):
    """
    represents a form used for validating and processing login data.
    """
    email = StringField("Email", validators=[
        DataRequired(), Email()
    ])

    password = StringField("Password", validators=[
        DataRequired(), Length(min=8, max=36), Regexp(regex=r'(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s])(?!.*\s).{8,}$')
    ])
