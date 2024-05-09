import secrets


class CustomUserServices:
    """
    CustomUser model services.
    Contains auxiliary methods for model operation.
     """

    @staticmethod
    def generate_password(length: int = 8) -> str:
        """ Generates valid password. """
        return secrets.token_urlsafe(length)
