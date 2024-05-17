import requests

from django.http import QueryDict

from rest_framework.exceptions import ValidationError, ParseError

import blog.settings as settings


def captcha_valid(
        request_data: QueryDict,
        endpoint: str = None,
        secret_key: str = None
) -> bool | None:
    """ Validates clients reCaptcha token. """

    key_check_endpoint = "https://www.google.com/recaptcha/api/siteverify"
    if not endpoint:
        token_validation_endpoint = key_check_endpoint
    else:
        token_validation_endpoint = endpoint

    client_token = request_data.get('g-recaptcha-response')

    if not client_token:
        raise ValidationError(detail="Captcha was not submitted.")

    payload = {
        "secret": secret_key if secret_key else settings.RECAPTCHA_SECRET_KEY,
        "response": client_token,
    }
    # returns a response from captcha server
    response = requests.post(token_validation_endpoint, params=payload).json()
    # extracting success value
    success = response.get("success")
    # returning success state if bool and rising an exception otherwise
    if isinstance(success, bool):
        return success
    else:
        raise ParseError(
            detail="Not valid captcha response. 'Success' value must"
            "be 'bool' but returned value is '{type(success)}'"
        )
