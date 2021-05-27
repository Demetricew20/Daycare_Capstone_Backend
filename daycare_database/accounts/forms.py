from django import forms
from .models import NewUser
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm


class CustomUserForm(UserCreationForm):
    """This form allows our custom user model to be registered with an added field reflecting its employee status"""
    is_daycare = forms.BooleanField(label="Check to register daycare", required=False)

    class Meta:
        model = NewUser
        fields = ("username", "password1", "password2", "is_daycare")

    def save(self, commit=True):
        # Overriding the save method to add user to auth group of Employee or Customer depending on if box is checked
        user = super(CustomUserForm, self).save(commit=False)
        user.is_daycare = self.cleaned_data["is_daycare"]

        if commit:
            user.save()
            if user.is_daycare:
                daycare = Group.objects.get(name="Daycares")
                daycare.user_set.add(user)
            else:
                parents = Group.objects.get(name="Parents")
                parents.user_set.add(user)
        return user
