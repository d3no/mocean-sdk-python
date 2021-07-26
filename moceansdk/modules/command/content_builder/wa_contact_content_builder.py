from moceansdk.exceptions import InvalidArgumentException
from moceansdk.modules.command.content_builder import AbstractContentBuilder
from moceansdk.modules.command.contact.wa_contact import WaContact


class WaContactContentBuilder(AbstractContentBuilder):
    def type(self):
        return "contact_detail"

    def required_key(self):
        return ["contact_detail"]

    def set_contact_detail(self, contact_detail: WaContact):
        self._params["contact_detail"] = contact_detail.get_request_data()
        return self
