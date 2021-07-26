from moceansdk.modules.command.mc_object.wa_mc_object_basic import WaMcObjectBasic
from moceansdk.modules.command.content_builder.wa_location_content_builder import WaLocationContentBuilder

class WaSendLocation(WaMcObjectBasic):

    def set_content(self, content: WaLocationContentBuilder):
        self._params['content'] = content.get_request_data()
        return self