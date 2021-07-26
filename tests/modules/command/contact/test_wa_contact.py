from unittest import TestCase

from moceansdk.modules.command.contact.wa_contact import WaContact


class TestWaContact(TestCase):
    def test_setter_return_type(self):
        obj = WaContact()
        self.assertIsInstance(obj.set_first_name("val"), WaContact)
        self.assertIsInstance(obj.set_last_name("val"), WaContact)
        self.assertIsInstance(obj.set_full_name("val"), WaContact)
        self.assertIsInstance(obj.set_phone_num("val"), WaContact)

    def test_is_required_key_set(self):
        required_keys = ["first_name", "last_name", "full_name", "phone_num"]
        self.assertEqual(WaContact().required_key(), required_keys)

    def test_params(self):
        params = {
            "full_name": "full_name",
            "first_name": "first_name",
            "last_name": "last_name",
            "phone_num": "phone_num",
        }

        obj = (
            WaContact()
            .set_first_name("first_name")
            .set_last_name("last_name")
            .set_full_name("full_name")
            .set_phone_num("phone_num")
        )

        self.assertEqual(obj.get_request_data(), params)
