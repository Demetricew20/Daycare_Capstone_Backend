from django.db import models
from django import forms


class User(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = forms.CharField(max_length=32)
    is_daycare = models.BooleanField(default=False)

    def __str__(self):
        return self.username
