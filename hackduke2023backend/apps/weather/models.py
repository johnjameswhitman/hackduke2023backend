from django.contrib.auth.models import User
from django.db import models


class WeatherAlertConfig(models.Model):
    """Configuration for an alert that a user is interested in."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=2)
