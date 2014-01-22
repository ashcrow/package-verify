
from . import TestCase

from package_verify.validator.loader import list_validators


class TestListValidators(TestCase):

    def test_list_validators(self):
        """
        Listing validators should return at least one item in a list
        """
        result = list_validators()
        assert result
        assert type(result) is list
