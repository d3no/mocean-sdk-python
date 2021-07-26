from unittest import TestCase

from moceansdk.modules.command.button import AbstractButton


class TestAbstractButton(TestCase):
    def test_throw_exception_if_calling_method_directly(self):
        try:
            AbstractButton().required_key()
            self.fail()
        except NotImplementedError:
            pass
