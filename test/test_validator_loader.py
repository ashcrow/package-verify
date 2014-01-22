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
Tests for loading validators by name,
"""

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
