from django import forms
from .models import Profile

class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']


# forms.py

from django import forms

class TimeForm(forms.Form):
    chosen_time = forms.DateTimeField(label='Выберите время', required=False)



