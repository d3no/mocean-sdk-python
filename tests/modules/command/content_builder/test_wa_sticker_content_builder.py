from unittest import TestCase

from moceansdk.modules.command.content_builder.wa_sticker_content_builder import (
    WaStickerConentBuilder,
)


class TestWaStickerContentBuilder(TestCase):
    def test_type(self):
        self.assertEqual(WaStickerConentBuilder().type(), "sticker")

    def test_request_data(self):
        params = {
            "rich_media_url": "rich_media_url",
            "text": "text",
            "type": "sticker",
        }

        obj = (
            WaStickerConentBuilder()
            .set_rich_media_url("rich_media_url")
            .set_text("text")
        )

        self.assertEqual(obj.get_request_data(), params)
