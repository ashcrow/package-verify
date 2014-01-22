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

    # Future proofing for multiple inputs
    for filename in args.manifest:
        try:
            with open(filename, 'r') as f_obj:
                validator.validate(f_obj.read())
        except IOError:
            parser.error(
                'The file "{0}" can not be opened'.format(filename))

    # Execute here
    exit_code = 0
    raise SystemExit(exit_code)


if __name__ == '__main__':
    main()
