# Copyright (C) 2014 Steve Milner
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
Tests the example specification validator.
"""

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
        assert type(result) == tuple
        for item in result:
            assert type(item) == list
            assert len(item) == 0

        # Something missing
        data2 = data
        del data2['files']
        result = validator.validate(json.dumps(data2))
        assert len(result[0]) == 0
        assert len(result[1]) == 1

        # Two items missing
        del data2['name']
        result = validator.validate(json.dumps(data2))
        assert len(result[0]) == 0
        assert len(result[1]) == 2

        # Bad data
        self.assertRaises(
            error.WrongFormatError, validator.validate, json.dumps(['hi']))

        # Not even JSON
        self.assertRaises(
            error.WrongFormatError, validator.validate, ['hi'])
