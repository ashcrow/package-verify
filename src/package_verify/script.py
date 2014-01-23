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
Command line entry point.
"""

import argparse

from package_verify.validator import loader


def main():
    """
    Script controller.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-q', '--quiet', action='store_true', default=False,
        help='Goes silent. Success/failure is only noted in the return code.')
    parser.add_argument(
        '-V', '--validator', type=str, default='devspec',
        choices=loader.list_validators(),
        help='Select a specific validator to use.'
    )
    parser.add_argument(
        'manifest', metavar='manifest', type=str, nargs=1,
        help='The manifest file to validate.')

    args = parser.parse_args()
    Validator = loader.load_validator(args.validator)
    validator = Validator()

    exit_code = 0
    # Future proofing for multiple inputs
    for filename in args.manifest:
        try:
            with open(filename, 'r') as f_obj:
                warnings, errors = validator.validate(f_obj.read())
                if not args.quiet:
                    for warning in warnings:
                        print "W: {0}".format(warning)
                    for error in errors:
                        print "E: {0}".format(error)

                if len(errors) > 0:
                    exit_code = 1
        except IOError:
            parser.error(
                'The file "{0}" can not be opened'.format(filename))

    # Execute here
    raise SystemExit(exit_code)


if __name__ == '__main__':
    main()
