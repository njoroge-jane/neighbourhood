from django import forms
from .models import Neighbour
#......

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Neighbour 
        exclude = ['neighbourhood_id','id']       
