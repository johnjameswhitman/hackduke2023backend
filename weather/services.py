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

    ALERTS_URL: str = "https://api.weather.gov/alerts/active"

    def get_alerts(self, config: WeatherAlertConfig) -> list[WeatherAlert]:
        """Fetches alerts for a given WeatherAlertConfig."""
        res = requests.get(
            self.ALERTS_URL,
            params={"area": config.state_abbreviation},
        )

        weather_alerts = []
        for alert_data in res.json().get("features", []):
            properties = alert_data["properties"]
            weather_alerts.append(
                WeatherAlert(
                    id=properties["id"],
                    status=WeatherAlertStatus(properties["status"]),
                    severity=WeatherAlertSeverity(properties["severity"]),
                    headline=properties["headline"],
                    description=properties["description"],
                    instruction=properties["instruction"],
                )
            )

        return weather_alerts
