from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser


class User(AbstractUser):
    is_daycare = models.BooleanField(default=False)

    def __str__(self):
        return self.username
