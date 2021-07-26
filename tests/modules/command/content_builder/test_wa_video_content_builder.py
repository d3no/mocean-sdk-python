from unittest import TestCase

from moceansdk.modules.command.content_builder.wa_video_content_builder import (
    WaVideoContentBuilder,
)


class TestWaVideoContentBuilder(TestCase):
    def test_type(self):
        self.assertEqual(WaVideoContentBuilder().type(), "video")

    def test_request_data(self):
        params = {
            "rich_media_url": "rich_media_url",
            "text": "text",
            "type": "video",
        }

        obj = (
            WaVideoContentBuilder()
            .set_rich_media_url("rich_media_url")
            .set_text("text")
        )

        self.assertEqual(obj.get_request_data(), params)
