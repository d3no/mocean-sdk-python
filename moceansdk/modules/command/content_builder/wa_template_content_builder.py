from typing import overload
from moceansdk.modules.command.content_builder import AbstractContentBuilder
from moceansdk.modules.command.template.wa_template_basic import WaTemplateBasic

class WaTemplateContentBuilder(AbstractContentBuilder):
    def type(self):
        return 'template'


    def required_key(self):
        return ['wa_template']

    def set_wa_template(self, wa_template: WaTemplateBasic):
        self._params['wa_template'] = wa_template.get_request_data()
        return self