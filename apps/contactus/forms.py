from django import forms
from django.forms import widgets
from .models import Contact,MailBook


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Contact
        exclude = ('created_at',)

    def is_valid(self):
        valid = super(ContactForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        contact_info = super(ContactForm, self).save(commit=False)
        
        if commit:
            contact_info.save()
        return contact_info

