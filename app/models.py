from django.db import models
import uuid
from accounts.models import *
from .constants import  CAR_BRANDS,TRANSMISSION_OPTIONS
from .utils import user_listing_path
# Create your models here.

class Listing(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True,editable=False)
    created_at=models.DateTimeField(auto_now_add=True)# add date and time when it is created
    updated_at=models.DateTimeField(auto_now=True) #update date and time field
    seller=models.ForeignKey(Profile,on_delete=models.CASCADE)
    brand=models.CharField(max_length=100,choices=CAR_BRANDS,default=None)
    mileage=models.IntegerField(default=0)
    color=models.CharField(max_length=24)
    model=models.CharField(max_length=24)
    description=models.TextField()
    engine=models.CharField(max_length=24)
    transmission=models.CharField(max_length=100,choices=TRANSMISSION_OPTIONS,default=None)
    location=models.OneToOneField(Location,on_delete=models.SET_NULL,null=True)
    image=models.ImageField(upload_to=user_listing_path)

    def __str__(self):
        return f'{self.seller.user.username}\'s Listing - {self.model}'

class LikedListing(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    like_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.listing.model} listing liked by {self.profile.user.username}'





