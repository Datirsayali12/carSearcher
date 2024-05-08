from django import forms
from .models import *
from django.contrib.auth.models import User

from .widget import CustomPictureImageFieldWidget


class UserForm(forms.ModelForm):
    username = forms.CharField(disabled=True)#no one can edit it

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    photo = forms.ImageField(widget=CustomPictureImageFieldWidget)
    bio = forms.TextInput()

    class Meta:
        model = Profile
        fields = ('photo', 'bio', 'phone_number')


class LocationForm(forms.ModelForm):

    address_1 = forms.CharField(required=True)


    class Meta:
        model = Location
        fields = {'address1', 'address2', 'city', 'state'}