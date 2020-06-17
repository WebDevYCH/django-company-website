from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
# Register your models here.
from .models import Employer
from agrosite.utils import get_current_site
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import UsernameField

import xadmin
from xadmin import views
from xadmin.sites import AdminSite
from django.contrib.sites.admin import SiteAdmin
from django.contrib.admin.models import LogEntry
from django.contrib.sites.models import Site
from agrosite.logentryadmin import LogEntryAdmin

class AgrositeAdminSite(AdminSite):
    site_header = 'DjangoBlog administration'
    site_title = 'DjangoBlog site admin'

    def __init__(self, name='admin'):
        super().__init__(name)



class EmployerCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='reenter the same password', widget=forms.PasswordInput)

    class Meta:
        model = Employer
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("passwords are not equal")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.source = 'adminsite'
            user.save()
        return user


class EmployerChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Raw passwords are not stored, so there is no way to see this "
            "user's password, but you can change the password using "
            "<a href=\"{}\">this form</a>."
        ),
    )
    email = forms.EmailField(label="Email", widget=forms.EmailInput)

    class Meta:
        model = Employer
        fields = '__all__'
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class EmployerAdmin(UserAdmin):
    form = EmployerChangeForm
    add_form = EmployerCreationForm
    list_display = ('id', 'nickname', 'username', 'email', 'last_login', 'date_joined', 'source')
    list_display_links = ('id', 'username')
    ordering = ('-id',)

admin_site = AgrositeAdminSite(name='admin')
admin_site.register(Employer, EmployerAdmin)
admin_site.register(Site, SiteAdmin)
admin_site.register(LogEntry, LogEntryAdmin)