from moceansdk.modules.command.button.wa_call_button import WaCallButton
from unittest import TestCase

from moceansdk.modules.command.template.wa_text_template import WaTextTemplate


class TestWaTextTemplate(TestCase):
    def test_type(self):
        self.assertEqual(WaTextTemplate().type(), "text")

    def test_request_data(self):
        wa_buttons = [WaCallButton()]
        params = {
            "name": "name",
            "language": "language",
            "body_params": ["body_params"],
            "header_params": ["header_params"],
            "wa_buttons": [wa_buttons[0].get_request_data()],
            "type": "text",
        }

        obj = (
            WaTextTemplate()
            .set_name("name")
            .set_language("language")
            .set_body_params(["body_params"])
            .set_header_params(["header_params"])
            .set_wa_buttons(wa_buttons)
        )

        self.assertEqual(obj.get_request_data(), params)
