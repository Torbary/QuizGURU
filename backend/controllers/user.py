from models import storage
from models.user import User
from validators.user import UserForm
from sqlalchemy.orm import scoped_session


@storage.with_session
def create_account(session, data):
    form: UserForm = UserForm(data=data)

    if not form.validate():
        return {"error": form.errors, "status": 400}, False
    else:
        user: scoped_session = (
            session.query(User).filter_by(email=data["email"]).first()
        )
        if user:
            return {
                "error": {"email": "an account exists with the provided email address"},
                "status": 409,
            }, False
        user = User(**data)
        user.save()
        return {"status": 201}, True
