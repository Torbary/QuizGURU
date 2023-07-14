from ..views import app_views
from controllers.quiz import get_quiz, fetch_quizzes
from controllers.question import fetch_questions
from flask import jsonify, request


@app_views.route("/quizzes/")
def quiz_gets():
    size = request.args.get("size", 50)
    page_index = request.args.get("page", 1)
    result = fetch_quizzes(page_size=size, page_no=page_index)

    return jsonify(result)

@app_views.route("/quizzes/<quiz_id>")
def quiz_get(quiz_id):
    result = get_quiz(quiz_id)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({"message": "quiz not found"}), 404


@app_views.route("/quizzes/<quiz_id>/questions")
def quiz_question_gets(quiz_id):
    result = fetch_questions(quiz_id=quiz_id)
    return jsonify(result)
