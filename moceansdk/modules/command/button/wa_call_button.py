from moceansdk.modules.command.button.wa_button_basic import WaButtonBasic


class WaCallButton(WaButtonBasic):
    def type(self):
        return "call"

    def required_key(self):
        return []
