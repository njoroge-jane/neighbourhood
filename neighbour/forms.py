from django import forms
from .models import Business, Neighbour
#......

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Neighbour 
        exclude = ['neighbourhood_id','id']  

class UploadForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user']

