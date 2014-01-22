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
An example validator.
"""

import json

from package_verify.validator import error, _Validator


class Validator(_Validator):

    expected_keys = (
        'name', 'version', 'release', 'license', 'summary', 'url', 'signature',
        'sha256', 'platform', 'scope', 'packager', 'source_name',
        'source_hash', 'scm_id', 'patches', 'dependencies', 'files',
        'config_files')

    non_strings = (
        ('patches', list),
        ('dependencies', dict),
        ('files', dict),
        ('config_files', dict),
    )

    def validate(self, data):
        errors = []
        warnings = []
        try:
            data = json.loads(data)
        except Exception, ex:
            print ex
            raise error.WrongFormatError('Input is not valid JSON')
        if type(data) != dict:
            raise error.WrongFormatError('Input data must be a dictionary')
        for key in self.expected_keys:
            try:
                assert key in data.keys()
            except AssertionError, ae:
                errors.append('{0} is missing'.format(key))

        for non_string in self.non_strings:
            try:
                if type(data[non_string[0]]) != non_string[1]:
                    errors.append('{0} must be a {1} not a {2]'.format(
                        non_string[0], non_string[1],
                        type(data[non_string[0]])))
            except KeyError:
                # Since we already noted that the key didn't exist we can
                # skip this exception
                pass

        return (warnings, errors)
