from django.db import models
from django.contrib.auth.models import User
from localflavor.in_.models import INStateField
from .utils import user_directory_path


class Location(models.Model):
    address1=models.CharField(max_length=100,blank=True)
    address2=models.CharField(max_length=100,blank=True)
    city=models.CharField(max_length=64)
    state=INStateField(default="NY")

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to=user_directory_path,null=True, default='userlogo.jpg')
    bio=models.CharField(max_length=100,blank=True)
    phone_number=models.CharField(max_length=12,blank=True)
    location=models.OneToOneField(Location,on_delete=models.SET_NULL,null=True)

    def __str__(self):
      return self.user.username



