#!/usr/bin/python3
"""
quiz model
"""

from datetime import datetime
from sqlalchemy import Column, String, Text, ForeignKey, Table
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.question import Question


class Quiz(BaseModel, Base):
    """
    Quiz model
    """
    __tablename__ = 'quizzes'
    description = Column(Text)
    title = Column(String(256), nullable=False)
    questions = relationship('Question', backref='quiz',
        cascade='all, delete-orphan')

user_quiz = Table('user_quiz', Base.metadata,
    Column('user_id', String(60), ForeignKey('users.id')),
    Column('quiz_id', String(60), ForeignKey('quizzes.id'))
)

