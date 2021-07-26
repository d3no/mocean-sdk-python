from moceansdk.modules.command.location.wa_location import WaLocation
from unittest import TestCase

from moceansdk.modules.command.template.wa_location_template import WaLocationTemplate
from moceansdk.modules.command.button.wa_call_button import WaCallButton
from moceansdk.modules.command.content_builder.wa_location_content_builder import (
    WaLocationContentBuilder,
)


class TestWaLocationTemplate(TestCase):
    def test_type(self):
        self.assertEqual(WaLocationTemplate().type(), "location")

    def test_is_required_key_set(self):
        required_key = ["name", "language", "body_params", "media_content"]
        obj = WaLocationTemplate()
        self.assertEqual(obj.required_key(), required_key)

    def test_request_data(self):
        wa_buttons = [WaCallButton()]
        media_content = WaLocationContentBuilder().set_location(
            WaLocation().set_latitude("latitude").set_longitude("longitude")
        )
        params = {
            "name": "name",
            "language": "language",
            "body_params": ["body_params"],
            "header_params": ["header_params"],
            "wa_buttons": [wa_buttons[0].get_request_data()],
            "media_content": media_content.get_request_data(),
            "type": "location",
        }

        obj = (
            WaLocationTemplate()
            .set_name("name")
            .set_language("language")
            .set_body_params(["body_params"])
            .set_header_params(["header_params"])
            .set_wa_buttons(wa_buttons)
            .set_media_content(media_content)
        )

        self.assertEqual(obj.get_request_data(), params)
