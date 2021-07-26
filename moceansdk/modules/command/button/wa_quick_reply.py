from moceansdk.modules.command.button.wa_button_basic import WaButtonBasic


class WaQuickReplyButton(WaButtonBasic):
    def type(self):
        return "quick_reply"

    def required_key(self):
        return ["quick_reply"]

    def set_quick_reply(self, quick_reply):
        self._params["quick_reply"] = quick_reply
        return self
