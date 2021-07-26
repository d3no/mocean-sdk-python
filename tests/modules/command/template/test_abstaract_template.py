from unittest import TestCase

from moceansdk.modules.command.template import AbstractTemplate


class TestAbstractTemplate(TestCase):
    def test_throw_exception_if_calling_method_directly(self):
        try:
            AbstractTemplate().required_key()
            self.fail()
        except NotImplementedError:
            pass
