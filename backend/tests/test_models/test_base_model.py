#!/usr/bin/python3
'''
contains test-cases for models.base_model
'''
import re
from models.base_model import BaseModel, Base
from models import Storage
import unittest
import os


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
    def setUp(self):
        self.storage = Storage()
        self.storage.drop()

    def tearDown(self):
        self.storage.drop()

    def test_attributes(self):
        model = TestBaseModel()
        model2 = TestBaseModel()
        self.assertTrue(check_uuid(model.id))
        self.assertTrue(check_uuid(model2.id))
        self.assertNotEqual(model.id, model2.id)
