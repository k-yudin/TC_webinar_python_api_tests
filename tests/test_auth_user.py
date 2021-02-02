from core.base_test import BaseCase
from core.my_request import Request
from core.asserts import Asserts


class TestCreateUser(BaseCase):
    def test_wrong_data(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response = Request.post('user/login', data)
        Asserts.assert_code_status(response, 400)
        Asserts.assert_response_text(response, "Invalid username/password supplied")
        Asserts.assert_response_not_has_cookie(response, 'auth_sid')
        Asserts.assert_response_not_has_headers(response, "x-csrf-token")

    def test_auth_successfully(self):
        email = 'vinkotov@example.com'
        password = '123'
        data = {
            'email': email,
            'password': password
        }

        response = Request.post('user/login', data)
        Asserts.assert_code_status(response, 200)
        Asserts.assert_response_has_cookie(response, 'auth_sid')
        Asserts.assert_response_has_headers(response, "x-csrf-token")
