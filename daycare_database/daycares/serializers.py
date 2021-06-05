from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model
User = get_user_model()


class DaycareSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=User.objects.all())

    class Meta:
        model = models.Daycare
        fields = ('id', 'url', 'user', 'name', 'city', 'state', 'zip_code', 'images', 'street_address',
                  'description', 'avg_rating', 'min_cost_infant', 'max_cost_infant', 'min_cost_youth_T', 'max_cost_youth_T',
                  'min_cost_old_T', 'max_cost_old_T', 'min_cost_preschool', 'max_cost_preschool',
                  'availability', 'infant_group', 'young_toddler_group', 'older_toddler_group',
                  'preschooler_group', 'school_age_group', 'age_groups')


class AgeGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.AgeGroup
        fields = ('group_name', )


class ChildSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Child
        fields = ('id', 'name', 'age_group')


class ParentSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=User.objects.all())

    class Meta:
        model = models.Parent
        fields = ('id', 'user', 'street_address', 'city', 'state', 'zip_code', 'selected_daycare', 'child')


class DaycareReviewSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=User.objects.all())
    
    class Meta:
        model = models.DaycareReview
        fields = ('user', 'daycare', 'review_text', 'review_rating')

