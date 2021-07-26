

from moceansdk.modules.command.location import AbstractLocation


class WaLocation(AbstractLocation):

    def required_key(self):
        return ['latitude', 'longitude']

    def set_latitude(self, latitude):
        self._params['latitude'] = latitude
        return self
    
    def set_longitude(self, longitude):
        self._params['longitude'] = longitude
        return self

    def set_accuracy(self, accuracy):
        self._params['accuracy'] = accuracy
        return self
    
    def set_name(self, name):
        self._params['name'] = name
        return self
    
    def set_address(self, address):
        self._params['address'] = address
        return self