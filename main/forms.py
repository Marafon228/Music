from django import forms
from .models import Profile

class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']