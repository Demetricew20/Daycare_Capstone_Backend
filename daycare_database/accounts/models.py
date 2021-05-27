from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, last_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Must be assigned to is_staff as superuser.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Must bew assigned to is_superuser as superuser.')

        return self.create_user(email, user_name, first_name, last_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, last_name, password, is_daycare, **other_fields):
        if not user_name:
            raise ValueError(_('Username is required'))
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, last_name=last_name,
                          is_daycare=is_daycare, **other_fields)
        user.set_password(password)
        user.save()
        if user.is_daycare:
            daycares = Group.objects.get(name='Daycares')
            daycares.user_set.add(user)
        else:
            parents = Group.objects.get(name='Parents')
            parents.user_set.add(user)
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=70, blank=True)
    last_name = models.CharField(max_length=70, blank=True)
    user_name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    is_daycare = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    if is_daycare is True:
        is_active = models.BooleanField(default=False)
    else:
        is_active = models.BooleanField(default=True)
    objects = CustomAccountManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'is_daycare', 'email']

    def __str__(self):
        return self.user_name
