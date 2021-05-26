from rest_framework import serializers
from . import models


class DaycareSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Daycare
        fields = ('id', 'user', 'url', 'name', 'city', 'state', 'zip_code', 'images', 'description',
                  'min_cost_estimate', 'max_cost_estimate', 'teacher_child_ratio',
                  'availability')

