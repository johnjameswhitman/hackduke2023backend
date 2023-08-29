"""Auth route for Ninja.

Borrowed from: https://github.com/vitalik/django-ninja/issues/45#issuecomment-1049829818
"""
from django.contrib.auth import authenticate
from django.http import HttpResponse
from ninja import Router, Schema
from rest_framework_simplejwt.tokens import RefreshToken

router = Router()


class LoginRequest(Schema):
    username: str
    password: str


class LoginResponse(Schema):
    refresh_token: str
    access_token: str


@router.post("/login", response=LoginResponse, auth=None)
def login(request, auth: LoginRequest):
    user = authenticate(**auth.dict())

    if not user:
        return HttpResponse("Unauthorized", status=401)

    refresh = RefreshToken.for_user(user)

    return LoginResponse(
        refresh_token=str(refresh),
        access_token=str(refresh.access_token),
    )
