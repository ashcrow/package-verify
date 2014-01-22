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
General Validator code.
"""

class _Validator(object):
    """
    Parent class for validators.
    """

    def validate(self, data):
        """
        Validates input data.
        """
        raise NotImplementedError('validate() must be implemented')

    def __repr__(self):
        """
        Code representation.
        """
        return "{0}()".format(self.__class__.__name__)

    def __str__(self):
        """
        String representation of the instance.
        """
        return "<{0}()>".format(self.__class__.__name__)

    def __unicode__(self):
        """
        Unicode representation of the instance.
        """
        return unicode(self.__str__())
