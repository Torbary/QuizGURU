#!/usr/bin/python3
import json
from models.quiz import Quiz
from models.question import Question
from models.user import User


def create_quiz(quiz=None):
	if not quiz:
		return None
	quiz_model = Quiz()
	quiz_model.title = quiz['title']
	quiz_model.description = quiz['description']
	return quiz_model

def create_question(question, quiz_id):
	if not question or not quiz_id:
		return
	question_model = Question(**question)
	question_model.quiz_id = quiz_id
	question_model.save()
	return question_model

def creation_questions(questions, quiz_id):
	if type(questions) is not list or not quiz_id:
		return None
	question_models = []
	for data in questions:
		question = create_question(data, quiz_id)
		question_models.append(question)
	return question_models

if __name__ == '__main__':

	with open("example.json", "r") as file:
		data = json.load(file)

	data = data.get('quiz')

	quiz = create_quiz(data)
	questions = creation_questions(data.get('questions'), quiz.id)
	quiz.questions = questions

	quiz.save()
