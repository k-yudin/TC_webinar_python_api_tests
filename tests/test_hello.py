from core.my_request import Request
from core.asserts import Asserts
from core.base_test import BaseCase


class TestHello(BaseCase):
    def test_call_wo_name(self):
        response = Request.get('/api/hello')
        Asserts.assert_code_status(response, 200)
        Asserts.assert_response_text(response, "Hello, someone")

    def test_call_with_name(self):
        name = 'Vitalii'
        response = Request.get('/api/hello', {'name': name})
        Asserts.assert_code_status(response, 200)
        Asserts.assert_response_text(response, f"Hello, {name}")
