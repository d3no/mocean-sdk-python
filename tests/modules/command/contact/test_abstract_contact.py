from unittest import TestCase

from moceansdk.modules.command.contact import AbstractContact


class TestAbstractContact(TestCase):
    def test_throw_exception_if_calling_method_directly(self):
        try:
            AbstractContact().required_key()
            self.fail()
        except NotImplementedError:
            pass
