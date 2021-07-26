from unittest import TestCase

from moceansdk.modules.command.button.wa_url_parameter_button import (
    WaUrlParameterButton,
)


class TestWaUrlParameter(TestCase):
    def test_type(self):
        self.assertEqual(WaUrlParameterButton().type(), "url")

    def test_setter_return(self):
        obj = WaUrlParameterButton()
        self.assertIsInstance(obj.set_url_parameter("url"), WaUrlParameterButton)

    def test_is_required_key_set(self):
        required_key = ["url_parameter"]
        obj = WaUrlParameterButton()
        self.assertEqual(obj.required_key(), required_key)

    def test_request_data(self):
        params = {
            "url_parameter": "url",
            "type": "url",
        }

        obj = WaUrlParameterButton()
        obj.set_url_parameter("url")

        self.assertEqual(obj.get_request_data(), params)
