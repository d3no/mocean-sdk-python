from moceansdk.modules.command.button.wa_button_basic import WaButtonBasic


class WaUrlParameterButton(WaButtonBasic):
    def type(self):
        return "url"

    def required_key(self):
        return ["url_parameter"]

    def set_url_parameter(self, url_parameter):
        self._params["url_parameter"] = url_parameter
        return self
