from core.my_request import Request
from core.asserts import Asserts
from core.base_test import BaseCase
import allure


class TestHello(BaseCase):
    @allure.description("Check API call without a name")
    def test_call_wo_name(self):
        response = Request.get('/api/hello')
        Asserts.assert_code_status(response, 200)
        Asserts.assert_response_text(response, "Hello, someone")

    @allure.description("Check API call with name")
    def test_call_with_name(self):
        name = 'Vitalii'
        response = Request.get('/api/hello', {'name': name})
        Asserts.assert_code_status(response, 200)
        Asserts.assert_response_text(response, f"Hello, {name}")
