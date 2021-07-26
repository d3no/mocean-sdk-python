from moceansdk.modules.command.template import wa_template_basic


class WaTextTemplate(wa_template_basic.WaTemplateBasic):

    def type(self):
        return 'text'