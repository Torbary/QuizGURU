from ..views import app_views
from controllers.quiz import get_quiz, fetch_quizzes, post_quiz, delete_quiz
from controllers.question import fetch_questions
from flask import jsonify, request, abort
from validators.quiz import QuizForm


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


@app_views.route("/quizzes", methods=["POST"])
def quiz_post():
    data = request.get_json()
    quiz_form: QuizForm = QuizForm(data=data)
    if not quiz_form.validate():
        errors = {"message": "invalid quiz data", "status_code": 400, "errors": {}}
        for k, v in quiz_form.errors.items():
            if type(v) is list:
                errors["errors"][k] = " ".join(v)
        return jsonify(errors), 400
    created = post_quiz(data)
    if not created:
        return jsonify({"message": "invalid quiz data"}), 400
    else:
        return jsonify({"message": "created"}), 201


@app_views.route("/quizzes/<quiz_id>", methods=["DELETE"])
def quiz_delete(quiz_id):
    deleted = delete_quiz(quiz_id)
    if deleted:
        return jsonify({}), 204
    else:
        return (
            jsonify(
                {
                    "message": "cannot delete the quiz referenced by the provided id, as it does not exist"
                }
            ),
            404,
        )
