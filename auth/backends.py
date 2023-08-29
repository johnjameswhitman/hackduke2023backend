"""Auth backend for Ninja.

Borrowed from: https://github.com/vitalik/django-ninja/issues/45#issuecomment-1049829818
"""
import logging
from typing import Any, Optional

from django.http import HttpRequest
from ninja.security import HttpBearer
from rest_framework_simplejwt.authentication import JWTAuthentication

logger = logging.getLogger(__name__)


# There may be a better way to do the below that automatically sets the request user, e.g.:
# https://github.com/vitalik/django-ninja/issues/305#issuecomment-1186234533
class JWTAuthRequired(HttpBearer):
    def authenticate(self, request: HttpRequest, token: str) -> Optional[Any]:
        """Authenticates request using JWT.

        Ninja will set request.auth using return value from this method.
        """
        jwt_authenticator = JWTAuthentication()
        try:
            response = jwt_authenticator.authenticate(request)
            if response is not None:
                user, _ = response
                request.user = user
                logger.debug("JWT authentication successful.", extra={"user": user})
                return user  # 200 OK
            return None  # 401
        except:
            # Any exception we want it to return False i.e 401
            logger.exception("Something went wrong authenticating JWT.")
            return None
