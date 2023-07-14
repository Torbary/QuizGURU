#!/usr/bin/python3
"""
user model
"""

from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.quiz import Quiz
from models.score import Score


class User(BaseModel, Base):
    """User model"""
    __tablename__ = "users"
    email = Column(String(128), unique=True, nullable=False)
    lastname = Column(String(128), nullable=False)
    firstname = Column(String(128), nullable=False)
    # types of role: user, admin
    type = Column(String(60), default="user")
    password = Column(String(128), nullable=False)
    quizzes = relationship('Quiz', secondary='user_quiz')
    scores = relationship('Score', backref='user')
