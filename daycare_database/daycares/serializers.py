from rest_framework import serializers
from . import models


class DaycareSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Daycare
        fields = ('id', 'user', 'url', 'name', 'city', 'state', 'zip_code', 'images', 'street_address',
                  'description', 'min_cost_estimate', 'max_cost_estimate', 'teacher_child_ratio',
                  'availability', 'infant_group', 'young_toddler_group', 'older_toddler_group',
                  'preschooler_group', 'school_age_group', 'age_groups')


class AgeGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.AgeGroup
        fields = ('group_name', )


class ChildSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Child
        fields = ('name', 'age_group')


class ParentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Parent
        fields = ('id', 'street_address', 'city', 'state', 'zip_code', 'selected_daycare', 'child')


class DaycareReviewSerializer(serializers.HyperlinkedModelSerializer):
    daycare = serializers.HyperlinkedRelatedField(view_name='daycare-detail', queryset=models.Daycare.objects.all())
    parent = serializers.HyperlinkedRelatedField(view_name='parent-detail', queryset=models.Parent.objects.all())
    
    class Meta:
        model = models.DaycareReview
        fields = ('daycare', 'parent', 'review_text', 'review_rating')

