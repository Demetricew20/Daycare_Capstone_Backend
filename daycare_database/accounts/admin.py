from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group


class UserAdminConfig(UserAdmin):

    ordering = ('user_name', )
    list_display = ('email', 'first_name', 'is_daycare', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name', 'last_name', )}),
        ('Permissions', {'fields': ('is_daycare',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_name', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_daycare')
        }),
    )

admin.site.register(NewUser, UserAdminConfig)
