
from package_verify.validator import error


def load_validator(name):
    """
    Loads and returns a validator class.
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
    """
    import os

    vpath = os.path.sep.join([os.path.dirname(error.__file__), 'validators'])
    validators = []
    for afile in os.listdir(vpath):
        if afile.endswith('.py') and not afile.startswith('_'):
            validators.append(afile[0:afile.rindex('.')])
    return validators
