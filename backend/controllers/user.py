"""
this module contains function for user management.
the return value of these functions looks like this:
    message, http status, dict/json object, boolean
"""
from functools import lru_cache
from models import storage
from models.user import User
from validators.user import UserForm, LoginForm
from sqlalchemy.orm import scoped_session, load_only

'''TODO
this is a memoization type of cache.
it's purpose is to reduce checking for "user_id" if it been seen already.
it's not a special thing... I'm talking about the "@lru_cache" decorator btw...
it's literally nothing though...
'''
@lru_cache(maxsize=20)
def is_auth(user_id):
    user = storage.get(User, user_id)
    return True if user else False


@storage.with_session
def create_account(session, data):
    """
    this function manages the creation of a user.
    the status code returned are as follows:
    * 400 - This returned when the data passed is invalid to create an account.
        a dict object containing information of the invalidation is returned as the error message.
    * 409 - Indicates there's a conflict because an account exists with the provided credential.
    * 201 - Indicates success as a new account is created.
    """
    form: UserForm = UserForm(data=data)

    if not form.validate():
        return form.errors, 400, False
    else:
        user: User | None = session.query(User).filter_by(email=data["email"]).first()
        if user:
            return (
                "an account exists with the provided credential",
                409,
                False,
            )
        user = User(**data)
        user.save()
        return "Successful", 201, True


@storage.with_session
def login_account(session: scoped_session, data):
    """
    this function logs the a user in, based on their credential.
    a 400 status code is returned due to invalid form submission.
    a 401 code is returned because the credentials provided are wrong.
    a 200 code indicating the account is logged in successfully.
    """
    form: LoginForm = LoginForm(data=data)

    # validate form
    if not form.validate():
        if form.errors.get("email"):
            field = "email"
            err_msg = "Please enter a valid email address."
        elif form.errors.get("password"):
            field = "password"
            err_msg = "password must contain at least one Uppercase, one number and one non-alphanumeric digit."

        return err_msg, 400, {field: err_msg}, False

    user = (
        session.query(User)
        .options(load_only(User.email, User.firstname, User.lastname, User.type))
        .filter_by(email=data["email"])
        .first()
    )
    if not user:
        return "user does not exist", 401, {"email": "user does not exist"}, False
    elif user.password != data["password"]:
        return "invalid credential", 401, {"password": "invalid credential"}, False
    else:
        return "valid credentials", 200, user.to_dict(), True
