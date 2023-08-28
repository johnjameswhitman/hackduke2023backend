from dataclasses import dataclass
from enum import Enum

import requests

from .models import WeatherAlertConfig


class WeatherAlertStatus(str, Enum):
    ACTUAL = "Actual"
    EXERCISE = "Exercise"
    SYSTEM = "System"
    TEST = "Test"
    DRAFT = "Draft"


class WeatherAlertSeverity(str, Enum):
    EXTREME = "Extreme"
    SEVERE = "Severe"
    MODERATE = "Moderate"
    MINOR = "Minor"
    UNKNOWN = "Unknown"


@dataclass
class WeatherAlert:
    """Lightweight entity based on Alert from Weather API.

    For docs see Schemas > Alert: https://www.weather.gov/documentation/services-web-api
    """

    id: str
    status: WeatherAlertStatus
    severity: WeatherAlertSeverity
    headline: str
    description: str
    instruction: str


class NationalWeatherService:
    """Utilities to retrieve data from the National Weather Service API.

    For docs see: https://www.weather.gov/documentation/services-web-api
    """

    def get_alerts(self, config: WeatherAlertConfig) -> list[WeatherAlert]:
        """Fetches alerts for a given WeatherAlertConfig."""
        res = requests.get(
            "https://api.weather.gov/alerts/active",
            params={"area": config.state_abbreviation},
        )

        weather_alerts = []
        for alert_data in res.json().get("features", []):
            weather_alerts.append(
                WeatherAlert(
                    id=alert_data["id"],
                    status=WeatherAlertStatus(alert_data["status"]),
                    severity=WeatherAlertSeverity(alert_data["severity"]),
                    headline=alert_data["headline"],
                    description=alert_data["description"],
                    instruction=alert_data["instruction"],
                )
            )

        return weather_alerts
