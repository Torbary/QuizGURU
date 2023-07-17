from functools import wraps
from ..views import app_views
from flask import jsonify, request, abort, session
from controllers.user import create_account, is_auth, login_account


def auth_required(func):
    """
    this decorator specifies that authentication is required.
    It's purpose is to protect a route from being accessed without
    the user being authenticated.
    for a user to be authenticated, the following are required:
    * user_id: user id that exists in the database.
    """

    @wraps(func)
    def decorated_func(*args, **kwargs):
        if "user_id" not in session:
            return jsonify({"message": "user not authenticated"}), 401
        elif is_auth(session["user_id"]):
            print("authenticated")
            return func(*args, **kwargs)
        else:
            return jsonify({"message": "user not authenticated"}), 401
    return decorated_func


@app_views.route("/register", methods=["POST"])
def account_create():
    form_data = request.get_json()
    err, _ = create_account(form_data)
    status = err["status"]
    return jsonify(err), status


@app_views.route("/users/<user_id>", methods=["GET"])
@auth_required
def user_get(user_id):
    name = "Welcome!"
    return f"{name}", 200

@app_views.route("/users/<user_id>", methods=["DELETE"])
@auth_required
def account_delete(user_id):
    return "User deletion Endpoint"

@app_views.route("/users/password", methods=["PUT"])
@auth_required
def change_password():
    return "Change password"


@app_views.route("/login", methods=["POST"])
def login_user():
    data = request.get_json()
    msg, status, res_data, state = login_account(data)
    if state == False:
        return jsonify(res_data), status
    else:
        session["user_id"] = res_data["id"]
        session["email"] = res_data["email"]
        return jsonify(res_data), status


@app_views.route("/logout", methods=["GET"])
@auth_required
def logout_user():
    session.clear()
    return "User logout", 200
