from moceansdk.modules.command.mc_object.wa_mc_object_basic import WaMcObjectBasic
from moceansdk.modules.command.content_builder.wa_sticker_content_builder import WaStickerConentBuilder

class WaSendSticker(WaMcObjectBasic):

    def set_content(self, content: WaStickerConentBuilder):
        self._params['content'] = content.get_request_data()
        return self