
from . import TestCase

from package_verify.validator import _Validator


class TestParserAbstraction(TestCase):

    def test_validation(self):
        """
        Verify abstraction layer does no validation on it's own.
        """
        self.assertRaises(NotImplementedError, _Validator().validate, {})

    def test_representation(self):
        """
        Validator should return a helpfule representation string.
        """
        assert repr(_Validator()) == '_Validator()'
