from unittest import TestCase

from moceansdk.modules.command.content_builder.wa_document_content_builder import (
    WaDocumentContentBuilder,
)


class TestWaDocumentContentBuilder(TestCase):
    def test_type(self):
        self.assertEqual(WaDocumentContentBuilder().type(), "document")

    def test_request_data(self):
        params = {
            "rich_media_url": "rich_media_url",
            "text": "text",
            "type": "document",
        }

        obj = (
            WaDocumentContentBuilder()
            .set_rich_media_url("rich_media_url")
            .set_text("text")
        )

        self.assertEqual(obj.get_request_data(), params)
