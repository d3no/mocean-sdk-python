from unittest import TestCase

from moceansdk.modules.command.button.wa_call_button import WaCallButton


class TestWaCallButton(TestCase):
    def test_type(self):
        self.assertEqual(WaCallButton().type(), "call")

    def test_request_data(self):
        params = {
            "type": "call",
        }

        obj = WaCallButton()

        self.assertEqual(obj.get_request_data(), params)
