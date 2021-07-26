from moceansdk.modules.command.contact import AbstractContact


class WaContact(AbstractContact):
    def required_key(self):
        return ["first_name", "last_name", "full_name", "phone_num"]

    def set_first_name(self, first_name):
        self._params["first_name"] = first_name
        return self

    def set_last_name(self, last_name):
        self._params["last_name"] = last_name
        return self

    def set_full_name(self, full_name):
        self._params["full_name"] = full_name
        return self

    def set_phone_num(self, phone_num):
        self._params["phone_num"] = phone_num
        return self
