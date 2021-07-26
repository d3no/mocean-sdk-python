from moceansdk.modules.command.content_builder import AbstractContentBuilder


class WaTextContentBuilder(AbstractContentBuilder):

    def type(self):
        return 'text'

    def required_key(self):
        return ['text']
    
    def set_text(self, text):
        self._params['text'] = text
        return self