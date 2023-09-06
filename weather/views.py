"""CRUD operations on Weather Alerts."""
import logging

from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import ModelSchema, Router, Schema

from .models import WeatherAlertConfig
from .services import NationalWeatherService, WeatherAlert

logger = logging.getLogger(__name__)
router = Router()


# Weather Alerts
class WeatherAlertRequest(Schema):
    state_abbreviation: str


class WeatherAlertResponse(ModelSchema):
    class Config:
        model = WeatherAlertConfig
        model_fields = "__all__"


class WeatherAlertDetailResponse(WeatherAlertResponse):
    alerts: list[WeatherAlert]

    @classmethod
    def from_model(cls, model: WeatherAlertConfig) -> "WeatherAlertDetailResponse":
        """Populates instance with model and response from National Weather Service API."""
        national_weather_service = NationalWeatherService()
        alerts = national_weather_service.get_alerts(model)
        kwargs = {**model.__dict__, "alerts": alerts}  # Merge model and alerts.
        return cls(**kwargs)  # "**" unpacks dict into keyword arguments.


@router.get("/alerts", response=list[WeatherAlertResponse])
def list_weather_alerts(request) -> list[WeatherAlertConfig]:
    return WeatherAlertConfig.objects.filter(user=request.auth)


@router.post("/alerts", response=WeatherAlertResponse)
def create_weather_alert(
    request: HttpRequest, data: WeatherAlertRequest
) -> WeatherAlertConfig:
    weather_alert_config = WeatherAlertConfig(
        user=request.auth, state_abbreviation=data.state_abbreviation.upper()
    )
    weather_alert_config.save()
    return weather_alert_config


@router.get("/alerts/{weather_alert_config_id}", response=WeatherAlertDetailResponse)
def read_weather_alert(
    request: HttpRequest, weather_alert_config_id: int
) -> WeatherAlertConfig:
    queryset = WeatherAlertConfig.objects.filter(user=request.auth)
    weather_alert_config = get_object_or_404(queryset, pk=weather_alert_config_id)
    return WeatherAlertDetailResponse.from_model(weather_alert_config)


@router.put("/alerts/{weather_alert_config_id}", response=WeatherAlertResponse)
def update_weather_alert(
    request: HttpRequest, weather_alert_config_id: int, data: WeatherAlertRequest
) -> WeatherAlertConfig:
    queryset = WeatherAlertConfig.objects.filter(user=request.auth)
    weather_alert_config = get_object_or_404(queryset, pk=weather_alert_config_id)
    for field, value in data.dict(exclude_none=True).items():
        setattr(weather_alert_config, field, value)
    weather_alert_config.save()
    return weather_alert_config


@router.delete("/alerts/{weather_alert_config_id}", response={204: None})
def delete_weather_alert(
    request: HttpRequest, weather_alert_config_id: int
) -> tuple[int, None]:
    queryset = WeatherAlertConfig.objects.filter(user=request.auth)
    weather_alert_config = get_object_or_404(queryset, pk=weather_alert_config_id)
    weather_alert_config.delete()
    return 204, None
