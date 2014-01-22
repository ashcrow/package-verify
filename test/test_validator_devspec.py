import json

from . import TestCase

from package_verify.validator import _Validator, error
from package_verify.validator.validators import devspec


data = {
    "name": "name",
    "version": "1.0.0",
    "release": "1",
    "license": "GPLv3",
    "summary": "A thing",
    "url": "http://example.com",
    "signature": "12345",
    "sha256": "12345",
    "platform": "",
    "scope": "/",
    "packager": "Someone",
    "source_name": "name-1.0.0.tar.gz",
    "source_hash": "12345",
    "scm_id": "r1234",
    "patches": [],
    "dependencies": {},
    "files": {},
    "config_files": {}
}


class TestDevspec(TestCase):

    def test_validator_creation(self):
        """
        Make sure the validator is created properly
        """
        result = devspec.Validator()
        assert type(result) is devspec.Validator
        assert issubclass(result.__class__, _Validator)

    def test_validation(self):
        """
        Make sure devspec properly validates input
        """
        validator = devspec.Validator()
        result = validator.validate(json.dumps(data))
        assert type(result) == list
        assert len(result) == 0

        # Something missing
        data2 = data
        del data2['files']
        result = validator.validate(json.dumps(data2))
        assert len(result) == 1

        # Two items missing
        del data2['name']
        result = validator.validate(json.dumps(data2))
        assert len(result) == 2

        # Bad data
        self.assertRaises(
            error.WrongFormatError, validator.validate, json.dumps(['hi']))

        # Not even JSON
        self.assertRaises(
            error.WrongFormatError, validator.validate, ['hi'])
