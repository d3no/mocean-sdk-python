from moceansdk.modules.command.mc_object import AbstractMc

class WaMcObjectBasic(AbstractMc):
    def action(self):
        return 'send-whatsapp'

    def required_key(self):
        return ['from', 'to', 'content']

    def set_from(self, id, type = 'bot_username'):
        self._params['from'] = {
            'type': type,
            'id': id
        }
        return self

    def set_to(self, id, type = 'phone_num'):
        self._params['to'] = {
            'type': type,
            'id': id,
        }
        return self
