from django.db import models


class Daycare(models.Model):
    user = models.ForeignKey('accounts.User', default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    zip_code = models.CharField(max_length=5, null=True)
    images = models.ImageField(null=True)
    description = models.CharField(max_length=250)
    min_cost_estimate = models.CharField(max_length=4)
    max_cost_estimate = models.CharField(max_length=4)
    teacher_child_ratio = models.CharField(max_length=15)
    availability = models.BooleanField(default=True)

class Parent(models.Model):
    pass


class AgeGroup(models.Model):
    pass


class AgeGroupRoles(models.Model):
    pass