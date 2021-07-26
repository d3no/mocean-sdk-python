from moceansdk.modules.command.template.wa_template_basic import WaTemplateBasic
from moceansdk.modules.command.content_builder.wa_photo_content_builder import (
    WaPhotoContentBuilder,
)


class WaPhotoTemplate(WaTemplateBasic):
    def type(self):
        return "photo"

    def required_key(self):
        required_key = super().required_key()
        required_key.append("media_content")
        return required_key

    def set_media_content(self, media_content: WaPhotoContentBuilder):
        self._params["media_content"] = media_content.get_request_data()
        return self
