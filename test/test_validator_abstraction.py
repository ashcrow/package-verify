
from . import TestCase

from package_verify.validator import _Validator


class TestParserAbstraction(TestCase):

    def test_validation(self):
        """
        Verify abstraction layer does no validation on it's own.
        """
        self.assertRaises(NotImplementedError, _Validator().validate, {})

    def test_representations(self):
        """
        Validator should return a helpful representation strings.
        """
        validator = _Validator()
        assert repr(validator) == '_Validator()'
        assert str(validator) == '<_Validator()>'
        assert unicode(validator) == unicode('<_Validator()>')
