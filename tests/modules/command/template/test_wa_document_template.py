from moceansdk.modules.command.template.wa_audio_template import WaAudioTemplate
from unittest import TestCase

from moceansdk.modules.command.template.wa_document_template import WaDocumentTemplate
from moceansdk.modules.command.button.wa_call_button import WaCallButton
from moceansdk.modules.command.content_builder.wa_document_content_builder import (
    WaDocumentContentBuilder,
)


class TestWaDocumentTemplate(TestCase):
    def test_type(self):
        self.assertEqual(WaDocumentTemplate().type(), "document")

    def test_is_required_key_set(self):
        required_key = ["name", "language", "body_params", "media_content"]
        obj = WaAudioTemplate()
        self.assertEqual(obj.required_key(), required_key)

    def test_request_data(self):
        wa_buttons = [WaCallButton()]
        media_content = WaDocumentContentBuilder().set_rich_media_url("url")
        params = {
            "name": "name",
            "language": "language",
            "body_params": ["body_params"],
            "header_params": ["header_params"],
            "wa_buttons": [wa_buttons[0].get_request_data()],
            "media_content": media_content.get_request_data(),
            "type": "document",
        }

        obj = (
            WaDocumentTemplate()
            .set_name("name")
            .set_language("language")
            .set_body_params(["body_params"])
            .set_header_params(["header_params"])
            .set_wa_buttons(wa_buttons)
            .set_media_content(media_content)
        )

        self.assertEqual(obj.get_request_data(), params)
