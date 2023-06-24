#!/usr/bin/python3
"""
answer model
"""

from datetime import datetime
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Answer(BaseModel, Base):
	__tablename__ = 'answers'
	question_id = Column(String(60), ForeignKey('questions.id'), nullable=False)
	answer = Column(Integer, nullable=False)
	quiz_id = Column(String(60), ForeignKey('quizzes.id'))
	score_id = Column(String(60), ForeignKey('scores.id'))
