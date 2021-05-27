from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):

    ordering = ('user_name', )
    list_display = ('email', 'first_name', 'is_daycare', 'is_active', 'is_staff')


admin.site.register(NewUser, UserAdminConfig)
