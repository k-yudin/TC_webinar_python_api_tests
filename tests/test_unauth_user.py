import pytest
import allure
from core.base_test import BaseCase
from core.my_request import Request
from core.asserts import Asserts


@allure.epic("Unauth cases")
class TestUnauthUser(BaseCase):
    @allure.description("This test is trying to get user data without id")
    def test_get_user_without_id(self):
        response = Request.get('user')

        Asserts.assert_code_status(response, 400)
        Asserts.assert_response_text(response, "Wrong HTTP method")
        Asserts.assert_time_is_less_than(response, 1)
