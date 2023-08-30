import logging
from enum import Enum
from typing import Optional

import requests
from ninja.schema import Schema

from .models import WeatherAlertConfig

logger = logging.getLogger(__name__)


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


class WeatherAlert(Schema):
    """Lightweight entity based on Alert from Weather API.

    For docs see Schemas > Alert: https://www.weather.gov/documentation/services-web-api
    """

    id: str
    status: WeatherAlertStatus
    severity: WeatherAlertSeverity
    headline: str
    description: str
    instruction: Optional[str]


class NationalWeatherService:
    """Utilities to retrieve data from the National Weather Service API.

    For docs see: https://www.weather.gov/documentation/services-web-api
    """

    ALERTS_URL: str = "https://api.weather.gov/alerts"

    def get_alerts(
        self, config: WeatherAlertConfig, limit: int = 10
    ) -> list[WeatherAlert]:
        """Fetches alerts for a given WeatherAlertConfig."""
        res = requests.get(
            self.ALERTS_URL,
            params={"area": config.state_abbreviation, "limit": limit},
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

        if weather_alerts:
            logger.debug("Found alerts.", extra={"count": len(weather_alerts)})
        else:
            logger.warning("Got no weather alerts!")

        return weather_alerts
