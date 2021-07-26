from unittest import TestCase

from moceansdk.modules.command.location import AbstractLocation


class TestAbstractContact(TestCase):
    def test_throw_exception_if_calling_method_directly(self):
        try:
            AbstractLocation().required_key()
            self.fail()
        except NotImplementedError:
            pass
