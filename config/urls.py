from auth.backends import JWTAuthRequired
from auth.views import router as auth_router
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from weather.views import router as weather_router

api = NinjaAPI(auth=JWTAuthRequired())
api.add_router("/auth/", auth_router)
api.add_router("/weather/", weather_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
