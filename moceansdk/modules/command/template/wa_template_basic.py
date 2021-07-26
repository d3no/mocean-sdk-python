from moceansdk.modules.command import button
from typing import List
from moceansdk.modules.command.template import AbstractTemplate
from moceansdk.modules.command.button.wa_button_basic import WaButtonBasic


class WaTemplateBasic(AbstractTemplate):
    def required_key(self):
        return ["name", "language", "body_params"]

    def set_name(self, name):
        self._params["name"] = name
        return self

    def set_language(self, language):
        self._params["language"] = language
        return self

    def set_body_params(self, body_params: list):
        self._params["body_params"] = body_params
        return self

    def set_header_params(self, header_params: list):
        self._params["header_params"] = header_params
        return self

    def set_wa_buttons(self, wa_buttons: List[WaButtonBasic]):
        func_get_request_data = lambda btn: btn.get_request_data()
        self._params["wa_buttons"] = list(map(func_get_request_data, wa_buttons))
        return self
