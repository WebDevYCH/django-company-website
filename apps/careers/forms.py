from django import forms
from django.forms import widgets
from .models import Job, Applicant, ApplicantDetails
import logging

logger = logging.getLogger(__name__)
class ApplyJobForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ('job',)

class ApplicantDetailsForm(forms.ModelForm):
    def __init__(self, job, user, *args, **kwargs):
        # self.job = None
        # if 'job' in kwargs:
        #     self.job = kwargs.pop('job')
        #     logger.info(self.job)
            # initial = kwargs.get('initial', {'job': kwargs.pop('job')})
            # data = {**initial, **data}
        self.job = job
        self.user = user
        super(ApplicantDetailsForm, self).__init__(*args, **kwargs)
        # logger.info(self.job)
        # self.fields['job'].initial = self.job
    class Meta:
        model = ApplicantDetails
        exclude = ('job','user','created_at',)
        labels = {
            "tenth_percent": "Tenth Percent",
            "puc_or_diploma": "Select Puc or Diplamo",
            "puc_or_diploma_marks": "Puc or Diplamo Marks",
            "degree_college": "Degree or College Name",
            "grade_or_percent": "Select Grade or Percent",
            "degree_marks":"Degree Marks",
        }

    def is_valid(self):
        valid = super(ApplicantDetailsForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        applicant = super(ApplicantDetailsForm, self).save(commit=False)
        
        if commit:
            applicant.user = self.user
            applicant.job = self.job
            applicant.save()
        return applicant
