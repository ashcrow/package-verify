

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
        return "<{0}>".format(self.__class__.__name__)

    def __unicode__(self):
        """
        Unicode representation of the instance.
        """
        return unicode(self.__str__())
