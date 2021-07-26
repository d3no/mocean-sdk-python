from moceansdk.modules.command.content_builder import AbstractContentBuilder
from moceansdk.modules.command.location.wa_location import WaLocation
from moceansdk.exceptions import InvalidArgumentException

class WaLocationContentBuilder(AbstractContentBuilder):

    def type(self):
        return 'location'

    def required_key(self):
        return ['location']

    def set_location(self, location:WaLocation):
        self._params['location'] = location.get_request_data()
        return self

