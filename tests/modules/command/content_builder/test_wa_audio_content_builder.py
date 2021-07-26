from unittest import TestCase

from moceansdk.modules.command.content_builder.wa_audio_content_builder import (
    WaAudioContentBuilder,
)


class TestWaAudioContentBuilder(TestCase):
    def test_type(self):
        self.assertEqual(WaAudioContentBuilder().type(), "audio")

    def test_request_data(self):
        params = {
            "rich_media_url": "rich_media_url",
            "text": "text",
            "type": "audio",
        }

        obj = (
            WaAudioContentBuilder()
            .set_rich_media_url("rich_media_url")
            .set_text("text")
        )

        self.assertEqual(obj.get_request_data(), params)
