"""CRUD operations on Weather Alerts."""

from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import ModelSchema, Router, Schema

from .models import WeatherAlertConfig

router = Router()


class WeatherAlertRequest(Schema):
    state_abbreviation: str


class WeatherAlertResponse(ModelSchema):
    foo: str = "bar"

    class Config:
        model = WeatherAlertConfig
        model_fields = "__all__"


@router.get("/alerts", response=list[WeatherAlertResponse])
def list_weather_alerts(request) -> list[WeatherAlertConfig]:
    return WeatherAlertConfig.objects.all()


@router.post("/alerts", response=WeatherAlertResponse)
def create_weather_alert(
    request: HttpRequest, data: WeatherAlertRequest
) -> WeatherAlertConfig:
    weather_alert_config = WeatherAlertConfig(
        state_abbreviation=data.state_abbreviation
    )
    weather_alert_config.save()
    return weather_alert_config


@router.get("/alerts/{weather_alert_config_id}", response={200: WeatherAlertResponse})
def read_weather_alert(
    request: HttpRequest, weather_alert_config_id: int
) -> WeatherAlertConfig:
    return get_object_or_404(WeatherAlertConfig, pk=weather_alert_config_id)


@router.put("/alerts/{weather_alert_config_id}", response=WeatherAlertResponse)
def update_weather_alert(
    request: HttpRequest, weather_alert_config_id: int, data: WeatherAlertRequest
) -> WeatherAlertConfig:
    weather_alert_config = get_object_or_404(
        WeatherAlertConfig, pk=weather_alert_config_id
    )
    for field, value in data.dict(exclude_none=True).items():
        setattr(weather_alert_config, field, value)
    weather_alert_config.save()
    return weather_alert_config


@router.delete("/alerts/{weather_alert_config_id}", response={204: None})
def delete_weather_alert(
    request: HttpRequest, weather_alert_config_id: int
) -> tuple[int, None]:
    weather_alert_config = get_object_or_404(
        WeatherAlertConfig, pk=weather_alert_config_id
    )
    weather_alert_config.delete()
    return 204, None