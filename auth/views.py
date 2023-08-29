"""Auth route for Ninja.

Borrowed from: https://github.com/vitalik/django-ninja/issues/45#issuecomment-1049829818
"""
from core.schemas import Error
from django.contrib.auth import authenticate
from ninja import Router, Schema
from rest_framework_simplejwt.tokens import RefreshToken

router = Router()


class LoginRequest(Schema):
    username: str
    password: str


class LoginResponse(Schema):
    refresh_token: str
    access_token: str


@router.post("/login", response={200: LoginResponse, 401: Error}, auth=None)
def login(request, auth: LoginRequest):
    user = authenticate(**auth.dict())

    if not user:
        return 401, Error(message="Unauthorized")

    refresh = RefreshToken.for_user(user)

    return LoginResponse(
        refresh_token=str(refresh),
        access_token=str(refresh.access_token),
    )
