from django import forms
from .models import Profile

class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']


# forms.py
from django import forms

from django import forms

from django import forms

class TimeForm(forms.Form):
    time = forms.TimeField(label='Выберите время', widget=forms.TimeInput(attrs={'type': 'time'}))



