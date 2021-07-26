from moceansdk.modules.command.template.wa_document_template import WaDocumentTemplate
from moceansdk.modules.command.contact.wa_contact import WaContact
from unittest import TestCase

from moceansdk.modules.command.template.wa_contact_template import WaContactTemplate
from moceansdk.modules.command.button.wa_call_button import WaCallButton
from moceansdk.modules.command.content_builder.wa_contact_content_builder import (
    WaContactContentBuilder,
)


class TestWaAudioTemplate(TestCase):
    def test_type(self):
        self.assertEqual(WaContactTemplate().type(), "contact_detail")

    def test_is_required_key_set(self):
        required_key = ["name", "language", "body_params", "media_content"]
        obj = WaContactTemplate()
        self.assertEqual(obj.required_key(), required_key)

    def test_request_data(self):
        wa_buttons = [WaCallButton()]
        media_content = WaContactContentBuilder().set_contact_detail(
            WaContact()
            .set_first_name("first_name")
            .set_last_name("last_name")
            .set_full_name("full_name")
            .set_phone_num("phone_num")
        )
        params = {
            "name": "name",
            "language": "language",
            "body_params": ["body_params"],
            "header_params": ["header_params"],
            "wa_buttons": [wa_buttons[0].get_request_data()],
            "media_content": media_content.get_request_data(),
            "type": "contact_detail",
        }

        obj = (
            WaContactTemplate()
            .set_name("name")
            .set_language("language")
            .set_body_params(["body_params"])
            .set_header_params(["header_params"])
            .set_wa_buttons(wa_buttons)
            .set_media_content(media_content)
        )

        self.assertEqual(obj.get_request_data(), params)
