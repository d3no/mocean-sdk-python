from moceansdk.modules.command.mc_object.wa_mc_object_basic import WaMcObjectBasic
from moceansdk.modules.command.content_builder.wa_contact_content_builder import WaContactContentBuilder

class WaSendContact(WaMcObjectBasic):

    def set_content(self, content: WaContactContentBuilder):
        self._params['content'] = content.get_request_data()
        return self