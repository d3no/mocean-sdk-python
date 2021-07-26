from unittest import TestCase

from moceansdk.modules.command.content_builder.wa_photo_content_builder import (
    WaPhotoContentBuilder,
)


class TestWaPhotoContentBuilder(TestCase):
    def test_type(self):
        self.assertEqual(WaPhotoContentBuilder().type(), "photo")

    def test_request_data(self):
        params = {
            "rich_media_url": "rich_media_url",
            "text": "text",
            "type": "photo",
        }

        obj = (
            WaPhotoContentBuilder()
            .set_rich_media_url("rich_media_url")
            .set_text("text")
        )

        self.assertEqual(obj.get_request_data(), params)
