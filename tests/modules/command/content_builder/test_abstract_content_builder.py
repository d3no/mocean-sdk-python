from unittest import TestCase

from moceansdk.modules.command.content_builder import AbstractContentBuilder


class TestAbstractContact(TestCase):
    def test_throw_exception_if_calling_method_directly(self):
        try:
            AbstractContentBuilder().required_key()
            self.fail()
        except NotImplementedError:
            pass
