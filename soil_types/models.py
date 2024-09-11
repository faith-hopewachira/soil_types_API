# soil_types/models.py
from django.db import models

class SoilType(models.Model):
    """
    This model shows the type of the soil, the description and the recommendation.

    Attributes
    soil_name: This shows the name of the soil.
    description: This shows the charactersitics of the soil
    recommendation: This outlines the recommendation of what to do with the type of the soil

    """
    soil_name = models.CharField(max_length=100)
    description = models.CharField(max_length=600)
    recommendation = models.CharField(max_length=700)

    def __str__(self):
        return self.soil_name
