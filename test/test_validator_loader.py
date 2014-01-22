
from . import TestCase

from package_verify.validator import _Validator
from package_verify.validator.error import UnknownValidatorError
from package_verify.validator.loader import load_validator


class TestValidatorLoader(TestCase):

    def test_load_validator(self):
        """
        Make sure loading a validator returns proper data.
        """
        result = load_validator('devspec')
        assert type(result) is type
        assert issubclass(result, _Validator)

    def test_fail_to_load_validator(self):
        """
        When a validator does not exist we should get a specific response
        """
        self.assertRaises(
            UnknownValidatorError, load_validator, 'doesnotexist')
