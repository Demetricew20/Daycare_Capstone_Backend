from django.db import models


class AgeGroup(models.Model):
    group_name = models.CharField(max_length=120, default=None)


class Daycare(models.Model):
    user = models.ForeignKey('accounts.User', default=None, on_delete=models.CASCADE)
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
    age = models.OneToOneField(AgeGroup, on_delete=models.CASCADE, default=None)


class Parent(models.Model):
    user = models.ForeignKey('accounts.User', default=None, on_delete=models.CASCADE),
    street_address = models.CharField(max_length=75, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    zip_code = models.CharField(max_length=5, null=True)
    selected_daycare = models.ManyToManyField(Daycare)
    child = models.ForeignKey(Child, default=None, on_delete=models.CASCADE)


class AgeGroupRoles(models.Model):
    group_id = models.ForeignKey(AgeGroup, default=None, on_delete=models.CASCADE)
    child = models.ForeignKey(Child, default=None, on_delete=models.CASCADE)


class DayCareReview(models.Model):
    daycare = models.OneToOneField(Daycare, on_delete=models.CASCADE)
    parent = models.OneToOneField(Parent, primary_key=True,  on_delete=models.CASCADE)
    review_text = models.CharField(max_length=120, default=None)
    review_rating = models.IntegerField(default=0)


