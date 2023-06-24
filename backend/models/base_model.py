#!/usr/bin/python3
"""
base model
"""

from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4

Base = declarative_base()


class BaseModel:
    """Base Model"""

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        instantiates a new model
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if not kwargs:
            from models import storage
            storage.new(self)
        else:
            format = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key in ('updated_at', 'created_at'):
                    value = datetime.strptime(value, format)
                if key != '__class__':
                    setattr(self, key, value)

    def save(self):
        """
        saves the model to the storage
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()
