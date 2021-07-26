from unittest import TestCase

from moceansdk.modules.command.location.wa_location import WaLocation


class TestWaLocation(TestCase):
    def test_is_required_key_set(self):
        required_key = ["latitude", "longitude"]
        obj = WaLocation()
        self.assertEqual(obj.required_key(), required_key)

    def test_setter_return(self):
        obj = WaLocation()
        self.assertIsInstance(obj.set_longitude("val"), WaLocation)
        self.assertIsInstance(obj.set_latitude("val"), WaLocation)
        self.assertIsInstance(obj.set_address("val"), WaLocation)
        self.assertIsInstance(obj.set_accuracy("val"), WaLocation)
        self.assertIsInstance(obj.set_name("val"), WaLocation)

    def test_request_data(self):
        params = {
            "longitude": "longitude",
            "latitude": "latitude",
            "address": "address",
            "accuracy": "accuracy",
            "name": "name",
        }

        obj = (
            WaLocation()
            .set_longitude("longitude")
            .set_latitude("latitude")
            .set_address("address")
            .set_accuracy("accuracy")
            .set_name("name")
        )

        self.assertEqual(obj.get_request_data(), params)
