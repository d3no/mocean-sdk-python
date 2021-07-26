from moceansdk.modules.command import contact
from moceansdk.modules.command.contact.wa_contact import WaContact
from unittest import TestCase

from moceansdk.modules.command.content_builder.wa_contact_content_builder import (
    WaContactContentBuilder,
)


class TestWaContactContentBuilder(TestCase):
    def test_type(self):
        self.assertEqual(WaContactContentBuilder().type(), "contact_detail")

    def test_is_required_key_test(self):
        required_key = ["contact_detail"]
        obj = WaContactContentBuilder()
        self.assertEqual(obj.required_key(), required_key)

    def test_request_data(self):
        contact_detail = (
            WaContact()
            .set_first_name("first_name")
            .set_last_name("last_name")
            .set_full_name("full_name")
            .set_phone_num("phone_num")
        )

        params = {
            "contact_detail": contact_detail.get_request_data(),
            "type": "contact_detail",
        }

        obj = WaContactContentBuilder().set_contact_detail(contact_detail)

        self.assertEqual(obj.get_request_data(), params)
