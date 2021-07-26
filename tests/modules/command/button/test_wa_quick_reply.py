from unittest import TestCase

from moceansdk.modules.command.button.wa_quick_reply import WaQuickReplyButton


class TestWaQuickReply(TestCase):
    def test_type(self):
        self.assertEqual(WaQuickReplyButton().type(), "quick_reply")

    def test_is_required_key_set(self):
        required_key = ["quick_reply"]
        obj = WaQuickReplyButton()
        self.assertEqual(obj.required_key(), required_key)

    def test_request_data(self):
        params = {
            "quick_reply": "quick_reply",
            "type": "quick_reply",
        }

        obj = WaQuickReplyButton()
        obj.set_quick_reply("quick_reply")

        self.assertEqual(obj.get_request_data(), params)
