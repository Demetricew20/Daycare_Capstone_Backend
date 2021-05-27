from django.db import models
from django.conf import settings


class AgeGroup(models.Model):
    group_name = models.CharField(max_length=120, default=None)


class Daycare(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    street_address = models.CharField(max_length=75, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    zip_code = models.CharField(max_length=5, null=True)
    images = models.ImageField(null=True)
    description = models.CharField(max_length=250)
    min_cost_estimate = models.CharField(max_length=4)
    max_cost_estimate = models.CharField(max_length=4)
    teacher_child_ratio = models.CharField(max_length=15)
    availability = models.BooleanField(default=True)
    infant_group = models.BooleanField(default=False)
    young_toddler_group = models.BooleanField(default=False)
    older_toddler_group = models.BooleanField(default=False)
    preschooler_group = models.BooleanField(default=False)
    school_age_group = models.BooleanField(default=False)
    age_groups = models.ManyToManyField(AgeGroup)


class Child(models.Model):
    name = models.CharField(max_length=120, default=None)
    age_group = models.OneToOneField(AgeGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Parent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, on_delete=models.CASCADE),
    street_address = models.CharField(max_length=75, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    zip_code = models.CharField(max_length=5, null=True)
    selected_daycare = models.ManyToManyField(Daycare, blank=True)
    child = models.ManyToManyField(Child)


class DaycareReview(models.Model):
    daycare = models.ManyToManyField(Daycare, default=None)
    parent = models.OneToOneField(Parent, default=None,  on_delete=models.CASCADE)
    review_text = models.CharField(max_length=120, null=True)
    review_rating = models.IntegerField(default=0)


