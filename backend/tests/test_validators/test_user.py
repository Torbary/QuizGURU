"""
unit-test cases for validators.user
"""

import unittest
from validators.user import UserForm


class TestUserForm(unittest.TestCase):
    def test_invalidate_missing_field(self):
        """
        test for missing field in provided user data
        """
        # the email field is missing
        data = {"lastname": "John", "firstname": "Doe", "password": "John123@"}

        user_form: UserForm = UserForm(data=data)
        valid = user_form.validate()

        self.assertFalse(valid, "missing field invalidation failed.")
        self.assertTrue(
            "email" in user_form.errors.keys(),
            "form invalidation did not signify an error.",
        )

    def test_invalidate_password(self):
        """
        the password field must contain atleast an uppercase,
        number and non-alphanumeric character, with a length of 8.
        """
        data = {
            "email": "example@company.com",
            "lastname": "John",
            "firstname": "Doe",
            "password": "john123@",
        }

        user_form: UserForm = UserForm(data=data)
        valid = user_form.validate()

        self.assertFalse(
            valid,
            "it's suppose to invalidate due to password field not containing an uppercase",
        )
        self.assertTrue(
            "password" in user_form.errors.keys(),
            "form invalidation did not signify an error.",
        )
