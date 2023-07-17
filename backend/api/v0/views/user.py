from ..views import app_views
from flask import jsonify, request, abort
from controllers.user import create_account

@app_views.route('/users', methods=['POST'])
def account_create():
    form_data = request.get_json()
    err, _ = create_account(form_data)
    status = err["status"]
    return jsonify(err), status

@app_views.route('/users/<user_id>', methods=['DELETE'])
def account_delete(user_id):
    return "User deletion Endpoint"

@app_views.route('/users/password', methods=['PUT'])
def change_password():
    return "Change password"


@app_views.route('/login', methods=['POST'])
def login_user():
    return "Login API endpoint"

@app_views.route('/logout', methods=['GET'])
def logout_user():
    return "Logout API endpoint"
