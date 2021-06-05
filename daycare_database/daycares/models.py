from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class AgeGroup(models.Model):
    group_name = models.CharField(max_length=120, default=None)


class Daycare(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    street_address = models.CharField(max_length=75, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    zip_code = models.CharField(max_length=5, null=True)
    images = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=250)
    avg_rating = models.IntegerField(default=0)
    min_cost_infant = models.CharField(max_length=4, null=True, blank=True)
    max_cost_infant = models.CharField(max_length=4, null=True, blank=True)
    #Youth toddler
    min_cost_youth_T = models.CharField(max_length=4, null=True, blank=True)
    max_cost_youth_T = models.CharField(max_length=4, null=True, blank=True)
    #Old toddler
    min_cost_old_T = models.CharField(max_length=4, null=True, blank=True)
    max_cost_old_T = models.CharField(max_length=4, null=True, blank=True)
    #Preschooler
    min_cost_preschool = models.CharField(max_length=4, null=True, blank=True)
    max_cost_preschool = models.CharField(max_length=4, null=True, blank=True)
    availability = models.BooleanField(default=True)
    infant_group = models.BooleanField(default=False)
    young_toddler_group = models.BooleanField(default=False)
    older_toddler_group = models.BooleanField(default=False)
    preschooler_group = models.BooleanField(default=False)
    school_age_group = models.BooleanField(default=False)
    age_groups = models.ManyToManyField(AgeGroup)


class Child(models.Model):
    name = models.CharField(max_length=120, default=None)
    age_group = models.ForeignKey(AgeGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Parent(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=75, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    zip_code = models.CharField(max_length=5, null=True)
    selected_daycare = models.ManyToManyField(Daycare, blank=True)
    child = models.ManyToManyField(Child)


class DaycareReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    daycare = models.ManyToManyField(Daycare, default=None)
    review_text = models.CharField(max_length=120, null=True)
    review_rating = models.IntegerField(default=0)


