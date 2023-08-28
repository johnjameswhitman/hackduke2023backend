import json
import pathlib
from typing import TextIO

import pytest
import responses

from ..models import WeatherAlertConfig
from ..services import NationalWeatherService


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

        fixture_path = (
            pathlib.Path(__file__).parent / f"fixtures/national_weather_service.json"
        )
        with fixture_path.open() as fixture_file:
            nws_data = json.load(fixture_file)

        # Below overrides the requests library get to the NWS API and forces it to return our fake data.
        mocked_responses.get(
            NationalWeatherService.ALERTS_URL,
            json=nws_data,
            status=200,
        )

        # Act
        weather_alerts = national_weather_service.get_alerts(config)

        # Assert
        assert weather_alerts
