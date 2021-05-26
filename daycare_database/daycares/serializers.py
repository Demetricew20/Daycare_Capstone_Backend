from rest_framework import serializers
from . import models


class DaycareSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Daycare
        fields = ('id', 'name', 'address', 'images', 'description'
                  'min_cost_estimate', 'max_cost_estimate', 'teacher_child_ratio',
                  'availability')

