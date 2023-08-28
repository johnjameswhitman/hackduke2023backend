"""Auth backend for Ninja.

Borrowed from: https://github.com/vitalik/django-ninja/issues/45#issuecomment-1049829818
"""
import logging
from typing import Any, Optional

from django.http import HttpRequest
from ninja.security import HttpBearer
from rest_framework_simplejwt.authentication import JWTAuthentication

logger = logging.getLogger(__name__)


class JWTAuthRequired(HttpBearer):
    def authenticate(self, request: HttpRequest, token: str) -> Optional[Any]:
        jwt_authenticator = JWTAuthentication()
        try:
            response = jwt_authenticator.authenticate(request)
            if response is not None:
                return True  # 200 OK
            return False  # 401
        except:
            # Any exception we want it to return False i.e 401
            logger.exception("Something went wrong authenticating JWT.")
            return False
