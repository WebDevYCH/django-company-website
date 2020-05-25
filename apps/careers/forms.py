from django import forms

from .models import Job, Applicant

class ApplyJobForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ('job',)
