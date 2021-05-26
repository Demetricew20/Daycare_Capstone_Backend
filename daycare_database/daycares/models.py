from django.db import models


class Daycare(models.Model):
    user = models.ForeignKey('accounts.user', default=0, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=175)
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