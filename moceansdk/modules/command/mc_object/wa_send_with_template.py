from moceansdk.modules.command.mc_object.wa_mc_object_basic import WaMcObjectBasic
from moceansdk.modules.command.content_builder.wa_template_content_builder import WaTemplateContentBuilder


class WaSendWithTemplate(WaMcObjectBasic):
    
    def set_content(self, content: WaTemplateContentBuilder):
        self._params['content'] = content.get_request_data()
        return self