from package_verify.error import VerifyError


class ValidationError(VerifyError):
    """
    Base class for validation errors.
    """
    pass


class WrongFormatError(ValidationError):
    """
    Raised if the format is wrong or broken.
    """
    pass


class MissingDataError(ValidationError):
    """
    Raised if there is expected data missing.
    """
    pass


class UnknownValidatorError(VerifyError):
    """
    Raised if the requested validator does not exist.
    """
    pass
