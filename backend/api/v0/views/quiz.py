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
    resp_data = {}
    status_code = None
    form, created = post_quiz(data)
    if created:
        resp_data = {"message": "created"}
        status_code = 201
    elif not created and len(form.errors) != 0:
        resp_data = {
            "message": "invalid quiz data",
            "status_code": 400,
            "errors": form.errors,
        }
        status_code = 400
    else:
        resp_data = {"message": "invalid quiz data", "status_code": 400}
        status_code = 400
    return jsonify(resp_data), status_code


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
