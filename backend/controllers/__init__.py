#!/usr/bin/python3
from models import storage
from sqlalchemy.orm import scoped_session
import re

class Singleton:
    _instance = None
    def __new__(self, *args, **kwargs):
        if not self._instance:
            self._instance = super().__new__(self)
        return self._instance

def is_uuidv4(input_string):
    pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    return re.match(pattern, input_string) is not None
