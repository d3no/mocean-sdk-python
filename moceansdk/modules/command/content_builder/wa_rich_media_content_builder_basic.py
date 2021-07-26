from moceansdk.modules.command.content_builder import AbstractContentBuilder


class WaRichMediaContentBuilderBasic(AbstractContentBuilder):
    def required_key(self):
        return ["rich_media_url"]

    def set_text(self, text):
        self._params["text"] = text
        return self

    def set_rich_media_url(self, rich_media_url):
        self._params["rich_media_url"] = rich_media_url
        return self
