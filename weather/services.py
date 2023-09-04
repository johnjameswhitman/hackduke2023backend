import logging
from enum import Enum
from functools import partial
from typing import Optional

import requests
from django.core.cache import cache
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
    headline: Optional[str]
    description: Optional[str]
    instruction: Optional[str]


class NationalWeatherService:
    """Utilities to retrieve data from the National Weather Service API.

    For docs see: https://www.weather.gov/documentation/services-web-api
    """

    ALERTS_URL: str = "https://api.weather.gov/alerts"
    ALERTS_CACHE_KEY_TEMPLATE: str = f"{__name__}.alerts.{{area}}.{{limit}}"

    def _get_alerts(self, area: str, limit: int) -> dict:
        """Fetches alerts from the NWS API."""
        res = requests.get(
            self.ALERTS_URL,
            params={"area": area, "limit": limit},
        )
        res.raise_for_status()  # Raises error if API returned HTTP 4XX or 5XX status.
        return res.json()

    def get_alerts(
        self, config: WeatherAlertConfig, limit: int = 10
    ) -> list[WeatherAlert]:
        """Fetches alerts for a given WeatherAlertConfig."""
        alerts = cache.get_or_set(
            self.ALERTS_CACHE_KEY_TEMPLATE.format(
                area=config.state_abbreviation, limit=limit
            ),
            # default can be a value or a zero-argument callable. "partial" takes a callable
            # (self._get_alerts) and its arguments (anything, but "area" and "limit" in this case),
            # and returns a new callable. This defers execution of self._get_alerts with the
            # given arguments until partial's return-value itself is called.
            default=partial(
                self._get_alerts, area=config.state_abbreviation, limit=limit
            ),
        )

        weather_alerts = []
        for alert_data in alerts.get("features", []):
            logger.info("Alert data.", extra=alert_data)
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
            logger.warning("Got no weather alerts!", extra={"area": config.state_abbreviation})

        return weather_alerts
