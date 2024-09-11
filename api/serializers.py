from rest_framework import serializers
from soil_types.models import SoilType

class SoilTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoilType
        fields = ['id', 'soil_name', 'description', 'recommendation']
