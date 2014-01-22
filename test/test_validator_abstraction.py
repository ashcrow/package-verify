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
Tests the _Validator base class.
"""

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
