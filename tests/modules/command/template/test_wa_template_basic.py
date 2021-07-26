from unittest import TestCase

from moceansdk.modules.command.template.wa_template_basic import WaTemplateBasic
from moceansdk.modules.command.button.wa_call_button import WaCallButton


class TestWaTemplateBasic(TestCase):
    def test_is_required_key_set(self):
        required_key = ["name", "language", "body_params"]
        obj = WaTemplateBasic()
        self.assertEqual(obj.required_key(), required_key)

    def test_setter_return(self):
        obj = WaTemplateBasic()
        self.assertIsInstance(obj.set_name("name"), WaTemplateBasic)
        self.assertIsInstance(obj.set_language("language"), WaTemplateBasic)
        self.assertIsInstance(obj.set_body_params(["body_params"]), WaTemplateBasic)
        self.assertIsInstance(obj.set_header_params(["header_params"]), WaTemplateBasic)
        self.assertIsInstance(obj.set_wa_buttons([WaCallButton()]), WaTemplateBasic)
