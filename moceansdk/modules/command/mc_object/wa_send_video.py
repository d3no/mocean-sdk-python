from moceansdk.modules.command.mc_object.wa_mc_object_basic import WaMcObjectBasic
from moceansdk.modules.command.content_builder.wa_video_content_builder import WaVideoContentBuilder

class WaSendVideo(WaMcObjectBasic):

    def set_content(self, content: WaVideoContentBuilder):
        self._params['content'] = content.get_request_data()
        return self