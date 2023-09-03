from django.contrib import admin

from weather.models import WeatherAlertConfig


class WeatherAlertConfigAdmin(admin.ModelAdmin):
    pass


admin.site.register(WeatherAlertConfig, WeatherAlertConfigAdmin)
