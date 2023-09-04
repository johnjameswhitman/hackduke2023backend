from django.contrib.auth.models import User
from django.db import models


class Severity(models.TextChoices):
    EXTREME = "Extreme"
    SEVERE = "Severe"
    MODERATE = "Moderate"
    MINOR = "Minor"
    UNKNOWN = "Unknown"


class WeatherAlertConfig(models.Model):
    """Configuration for an alert that a user is interested in."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state_abbreviation = models.CharField(max_length=2)
    severity = models.CharField(
        max_length=10,
        choices=Severity.choices,
        # Below options allow users to omit a severity if they want everything.
        blank=True,
        null=True,
    )
