from moceansdk.modules.command.mc_object.wa_mc_object_basic import WaMcObjectBasic
from moceansdk.modules.command.content_builder.wa_audio_content_builder import WaAudioContentBuilder

class WaSendAudio(WaMcObjectBasic):

    def set_content(self, content: WaAudioContentBuilder):
        self._params['content'] = content.get_request_data()
        return self