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
