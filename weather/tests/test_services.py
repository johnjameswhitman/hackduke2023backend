import json
import pathlib

import pytest
import responses

from ..models import WeatherAlertConfig
from ..services import NationalWeatherService
from .fixtures import get_text_fixture


@pytest.fixture(scope="function")
def mocked_responses():
    """Returns a mock that you can use to fake responses from calls to the requests library.

    MAGIC WARNING: pytest will 'inject' mocked_responses wherever you specify it as an argument to a test method.
    """
    with responses.RequestsMock() as _mocked_responses:
        yield _mocked_responses


class TestNationalWeatherService:
    def test_get_alerts(self, mocked_responses):
        """Confirms the NationalWeatherService class can parse API response."""
        # Arrange
        config = WeatherAlertConfig(state_abbreviation="NC")
        national_weather_service = NationalWeatherService()
        nws_data = json.loads(get_text_fixture("national_weather_service.json"))

        # Below overrides the requests library get to the NWS API and forces it to return our fake data.
        mocked_responses.get(
            NationalWeatherService.ALERTS_URL,
            json=nws_data,
            status=200,
        )

        # Act
        weather_alerts = national_weather_service.get_alerts(config)

        # Assert
        assert len(weather_alerts) == 3
        assert (
            "urn:oid:2.49.0.1.840.0.f4b98ce74ca69c0fd4f347d2aa8e1b03efdd4bdf.001.1"
            in [weather_alert.id for weather_alert in weather_alerts]
        )
