from unittest import TestCase

from moceansdk.modules.command.content_builder.wa_rich_media_content_builder_basic import (
    WaRichMediaContentBuilderBasic,
)


class TestWaRichMediaContentBuilderBasic(TestCase):
    def test_required_key(self):
        required_key = ["rich_media_url"]
        obj = WaRichMediaContentBuilderBasic()
        self.assertEqual(obj.required_key(), required_key)

    def test_is_required_key_not_set(self):
        required_key = ['rich_media_url']
        obj = WaRichMediaContentBuilderBasic()
        self.assertEqual(obj.required_key(), required_key)
        
    def test_setter_return(self):
        obj = WaRichMediaContentBuilderBasic()

        self.assertIsInstance(obj.set_text("val"), WaRichMediaContentBuilderBasic)
        self.assertIsInstance(
            obj.set_rich_media_url("url"), WaRichMediaContentBuilderBasic
        )
