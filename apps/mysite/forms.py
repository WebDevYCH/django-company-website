from django import forms

from apps.blog.models import Job, Applicant

class ApplyJobForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ('job',)
