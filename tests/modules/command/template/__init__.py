from unittest import TestCase

from moceansdk.modules.command.template.wa_audio_template import WaAudioTemplate
from moceansdk.modules.command.button.wa_call_button import WaCallButton
from moceansdk.modules.command.content_builder.wa_audio_content_builder import (
    WaAudioContentBuilder,
)


class TestWaAudioTemplate(TestCase):
    def test_type(self):
        self.assertEqual(WaAudioTemplate().type(), "text")

    def test_is_required_key_set(self):
        required_key = ["name", "language", "body_params", "media_url"]
        obj = WaAudioTemplate()
        self.assertEqual(obj.required_key(), required_key)

    def test_request_data(self):
        wa_buttons = [WaCallButton()]
        media_content = WaAudioContentBuilder().set_rich_media_url("url")
        params = {
            "name": "name",
            "language": "language",
            "body_params": ["body_params"],
            "header_params": ["header_params"],
            "wa_buttons": wa_buttons,
            "media_content": media_content.get_request_data(),
            "type": "text",
        }

        obj = (
            WaAudioTemplate()
            .set_name("name")
            .set_language("set_language")
            .set_body_params(["body_params"])
            .set_header_params(["header_params"])
            .set_wa_buttons(wa_buttons)
            .set_media_content(media_content)
        )

        self.assertEqual(obj.get_request_data(), params)
