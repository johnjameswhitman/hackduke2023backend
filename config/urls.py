from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from weather.views import router as weather_router

api = NinjaAPI()
api.add_router("/weather/", weather_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
