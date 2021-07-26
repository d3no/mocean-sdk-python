from moceansdk.modules.command.template.wa_template_basic import WaTemplateBasic
from moceansdk.modules.command.content_builder.wa_video_content_builder import (
    WaVideoContentBuilder,
)


class WaVideoTemplate(WaTemplateBasic):
    def type(self):
        return "video"

    def required_key(self):
        required_key = super().required_key()
        required_key.append("media_content")
        return required_key

    def set_media_content(self, media_content: WaVideoContentBuilder):
        self._params["media_content"] = media_content.get_request_data()
        return self
