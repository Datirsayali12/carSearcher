from django import forms
from .models import *

class ListingForm(forms.ModelForm):
    image=forms.ImageField(required=False)# make field required or not
    class Meta:
        model=Listing
        fields = {'brand', 'model', 'mileage',
                  'color', 'description', 'engine', 'transmission', 'image'}