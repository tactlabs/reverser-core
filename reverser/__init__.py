__version__ = '0.0.2'


class RevClient():
    """Rev client class
    """

    def __init__(self):
        """Basic initialization.

        .. note::
            The '*env*' parameter only accepts the following values:
                * '*dev*': for Reverser DEV server
                * '*qa*': for Reverser QA server

        :param username: Reverser username
        :type username: str
        """
        pass

    def rev_me(self, content):
        """Reverse the content

        :param content: content
        :type content: str
        :returns: Response str
        :rtype: str
        """
        
        return content[::-1]