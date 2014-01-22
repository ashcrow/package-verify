from package_verify.validator import error, _Validator


class Validator(_Validator):

    expected_keys = (
        'name', 'version', 'release', 'license', 'summary', 'url', 'signature',
        'sha256', 'platform', 'scope', 'packager', 'source_name',
        'source_hash', 'scm_id', 'patches', 'dependencies', 'files',
        'config_files')
    '''
        'patches': list,
#        'dependencies': (dict, (str, str)),
        'files': (dict, (str, str)),
#        'config_files': (dict, (dict, (str, bool))),
    }'''

    def validate(self, data):
        errors = []
        if type(data) != dict:
            raise error.WrongFormatError('Input data must be a dictionary')
        for key in self.expected_keys:
            try:
                assert key in data.keys()
            except AssertionError, ae:
                errors.append('{0} is missing'.format(key))
#                raise error.MissingDataError(key)

        assert type(data['patches']) == list
        assert type(data['dependencies']) == dict
        assert type(data['files']) == dict
        assert type(data['config_files']) == dict
