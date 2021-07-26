from unittest import TestCase

from moceansdk.modules.command.template.wa_video_template import WaVideoTemplate
from moceansdk.modules.command.button.wa_call_button import WaCallButton
from moceansdk.modules.command.content_builder.wa_video_content_builder import (
    WaVideoContentBuilder,
)


class TestWaVideoTemplate(TestCase):
    def test_type(self):
        self.assertEqual(WaVideoContentBuilder().type(), "video")

    def test_request_data(self):
        wa_buttons = [WaCallButton()]
        media_content = WaVideoContentBuilder().set_rich_media_url("url")
        params = {
            "name": "name",
            "language": "language",
            "body_params": ["body_params"],
            "header_params": ["header_params"],
            "wa_buttons": [wa_buttons[0].get_request_data()],
            "media_content": media_content.get_request_data(),
            "type": "video",
        }

        obj = (
            WaVideoTemplate()
            .set_name("name")
            .set_language("language")
            .set_body_params(["body_params"])
            .set_header_params(["header_params"])
            .set_wa_buttons(wa_buttons)
            .set_media_content(media_content)
        )

        self.assertEqual(obj.get_request_data(), params)
