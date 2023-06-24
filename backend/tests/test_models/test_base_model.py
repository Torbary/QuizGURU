#!/usr/bin/python3
'''
contains test-cases for models.base_model
'''
import re
from models.base_model import BaseModel, Base
from models import storage
import unittest


def check_uuid(string):
    '''
    check if the provided string is a uuid.
    this is done using regex
    '''

    # uuid regex pattern
    pattern = r'([a-fA-F0-9]{8})-([a-fA-F0-9]{4}-){3}([a-fA-F0-9]{12})'
    match = re.match(pattern, string)

    return True if match else False


class TestBaseModel(BaseModel, Base):
    __tablename__ = 'testbasemodel'
    pass


class test_BaseModel(unittest.TestCase):
    def test_attributes(self):
        storage.drop()
        model = TestBaseModel()
        model2 = TestBaseModel()
        self.assertTrue(check_uuid(model.id))
        self.assertTrue(check_uuid(model2.id))
        self.assertNotEqual(model.id, model2.id)
        storage.drop()
