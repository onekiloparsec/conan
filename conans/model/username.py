from conans.errors import InvalidNameException
import re


class Username(str):

    base_er = "[a-zA-Z][a-zA-Z0-9_-]{1,49}"
    pattern = re.compile("^%s$" % base_er)

    def __new__(cls, name):
        """Simple name creation.

        @param name:        string containing the desired name
        @param validate:    checks for valid simple name. default True
        """
        Username.validate(name)
        return str.__new__(cls, name)

    @staticmethod
    def validate(name, pattern=False):
        """Check for name compliance with pattern rules. User names can be
           with upper/lower case
        """
        if Username.pattern.match(name) is None:
            if pattern and name == "*":
                return
            if len(name) > 30:
                message = "'%s' is too long. Valid names must contain at most 30 characters."
            elif len(name) < 2:
                message = "'%s' is too short. Valid names must contain at least 2 characters."
            else:
                message = "'%s' is an invalid name. "\
                          "Valid names should begin with alphanumerical characters."
            raise InvalidNameException(message % name)
