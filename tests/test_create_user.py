from core.base_test import BaseCase
from core.my_request import Request
from core.asserts import Asserts


class TestCreateUser(BaseCase):

    def test_no_email(self):
        data = {
            'password': '123',
            'username': 'vinkotov',
            'firstName': 'Vitalii',
            'lastName': 'Kotov',
        }

        response = Request.post('user', data)
        Asserts.assert_code_status(response, 400)
        Asserts.assert_response_text(response, "The following required params are missed: email")

    def test_email_is_already_in_system(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '123',
            'username': 'vinkotov',
            'firstName': 'Vitalii',
            'lastName': 'Kotov',
        }

        response = Request.post('user', data)
        Asserts.assert_code_status(response, 400)
        Asserts.assert_response_text(response, f"Users with email '{data['email']}' already exists")

    def test_username_is_too_short(self):
        data = {
            'email': self.create_unique_email('test'),
            'password': '123',
            'username': 'v',
            'firstName': 'Vitalii',
            'lastName': 'Kotov',
        }

        response = Request.post('user', data)
        Asserts.assert_code_status(response, 400)
        Asserts.assert_response_text(response, "The value of 'username' field is too short")
