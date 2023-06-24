#!/usr/bin/python3
'''
contains test cases for storage module
'''
import unittest
from models import storage, Storage
from models.quiz import Quiz

class test_Storage(unittest.TestCase):
    """
    class to test the storage method
    """

    def setUp(self):
        self.storage = Storage()
        self.storage.drop()

    def tearDown(self):
        self.storage.drop()

    def test_singleton(self):
        storage1 = Storage()
        self.assertTrue(storage is self.storage)
        self.assertTrue(storage is storage1)
        self.assertTrue(self.storage is storage1)

    def test_new(self):
        quiz = Quiz()
        quiz.title = "A random quiz"
        quiz.save()
        quizzes = self.storage.all(Quiz)

        self.assertTrue(quiz in quizzes)

    def test_delete(self):
        quizzes = self.storage.all(Quiz)
        len_0 = len(quizzes)

        if len_0 > 0:
            self.storage.delete(quizzes[0])
            self.storage.save()
            quizzes = self.storage.all(Quiz)
            len_1 = len(quizzes)
            self.assertNotEqual(len_0, len_1)
        pass
