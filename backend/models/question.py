#!/usr/bin/python3
"""
question model
"""

from datetime import datetime
from sqlalchemy import Column, String, Text, JSON, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Question(BaseModel, Base):
    """
    Question model
    """
    __tablename__ = 'questions'
    question = Column(Text, nullable=False)
    options = Column(JSON, nullable=False)
    correct = Column(Integer, nullable=False)
    hint = Column(Text)
    point = Column(Integer, default=1)
    quiz_id = Column(String(60), ForeignKey('quizzes.id'))
    '''
    quiz is implicitly defined due to the relationship between
    Quiz and Question. check Quiz.questions attribute.
    '''