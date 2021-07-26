from moceansdk.modules.command.mc_object.wa_mc_object_basic import WaMcObjectBasic
from moceansdk.modules.command.content_builder.wa_photo_content_builder import WaPhotoContentBuilder

class WaSendPhoto(WaMcObjectBasic):

    def set_content(self, content: WaPhotoContentBuilder):
        self._params['content'] = content.get_request_data()
        return self