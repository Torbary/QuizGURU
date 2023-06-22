#!/usr/bin/python3
"""
answer model
"""

from datetime import datetime
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
import os
from models.base_model import BaseModel, Base
from models.answer import Answer
from models.quiz import Quiz


class Score(BaseModel, Base):
	__tablename__ = 'scores'
	score = Column(Integer, nullable=False, default=0)
	answers = relationship('Answer', backref='score', cascade='all, delete-orphan')
	quiz_id = Column(String(60), ForeignKey("quizzes.id"))
	user_id = Column(String(60), ForeignKey("users.id"))
	"""
	user is implicitly defined, due to the relationship
	between User and Score. check User.scores attribute for
	more info.
	"""
