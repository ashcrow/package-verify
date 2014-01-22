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
Helper functions for validators.
"""

from package_verify.validator import error


def load_validator(name):
    """
    Loads and returns a validator class.

    :param name str: The name of the validator class to load.
    :rtype: Validator
    :returns: Validator class
    """
    try:
        mod = __import__(
            'package_verify.validator.validators.{0}'.format(name),
            fromlist=['True'])
        return getattr(mod, 'Validator')
    except ImportError, ie:
        msg = 'No such validator: {0}'.format(str(ie))
        raise error.UnknownValidatorError(msg)


def list_validators():
    """
    Returns a lists all available validators.

    :rtype: list
    :returns: A list of available validators as strings.
    """
    import os

    vpath = os.path.sep.join([os.path.dirname(error.__file__), 'validators'])
    validators = []
    for afile in os.listdir(vpath):
        if afile.endswith('.py') and not afile.startswith('_'):
            validators.append(afile[0:afile.rindex('.')])
    return validators
