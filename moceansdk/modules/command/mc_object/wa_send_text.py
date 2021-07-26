from moceansdk.modules.command.mc_object.wa_mc_object_basic import WaMcObjectBasic
from moceansdk.modules.command.content_builder.wa_text_content_builder import WaTextContentBuilder

class WaSendText(WaMcObjectBasic):
  
    def set_content(self, content:WaTextContentBuilder):
        self._params['content'] = content.get_request_data()
        return self

    