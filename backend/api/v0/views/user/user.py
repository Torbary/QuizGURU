from api.v0.views import app_views
from .auth import auth_required
from controllers.user import fetch_user_quizzes, update_user_score, add_quiz_to_user
from controllers.score import create_score, calculate_score
from flask import jsonify, session, request


@app_views.get("/users/<user_id>/quizzes")
@auth_required
def user_quizzes_get(user_id):
    """
    route handler to fetch quizzes of user with `User.id == user_id`.
    Note: the quizzes retrieved are the ones that `user_id` has worked on.
    """
    if session["user_id"] != user_id:
        return "Unforbidden", 403
    quizzes = fetch_user_quizzes(user_id)

    return jsonify(quizzes)


@app_views.post("/users/<user_id>/quizzes")
@auth_required
def user_quizzes_post(user_id):
    """
    route handler for uploading answers to the database.
    """
    session_user = session["user_id"]
    if session_user != user_id:
        return "Forbidden", 403
    data = request.get_json()
    quiz_id = data["quiz_id"]

    msg, status, value, created = create_score(data, user_id)

    if not created:
        if value == None:
            return msg, status.value
        else:
            return jsonify(msg), status.value
    else:
        update_user_score(user_id, value)
        add_quiz_to_user(user_id, quiz_id)

        return f"{value.id}", status.value
