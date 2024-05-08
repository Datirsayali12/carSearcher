from importlib import reload

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .models import *
from .forms import *
from accounts.forms import *
from . filters import ListingFilter

# Create your views here.

def home_page(request):
    return  render(request,"app/home.html")


@login_required
def login_home(request):
    listings=Listing.objects.all()
    listing_filter = ListingFilter(request.GET, queryset=listings)
    user_liked_listings = LikedListing.objects.filter(
        profile=request.user.profile).values_list('listing')
    liked_listings_ids = [l[0] for l in user_liked_listings]
    return render(request,'app/login_home.html',{'listing_filter':listing_filter, 'liked_listings_ids': liked_listings_ids})

def list_view(request):
    if request.method=="POST":
        try:
            listing_forms=ListingForm(request.POST,request.FILES)
            location_forms=LocationForm(request.POST)
            if listing_forms.is_valid() and location_forms.is_valid():
                listing=listing_forms.save(commit=False)
                listing_location=location_forms.save()
                listing.seller=request.user.profile
                listing.location=listing_location
                listing.save()
                messages.info(
                    request, f'{listing.model} Listing Posted Successfully!')
                return redirect('login_home')
        except Exception as e:
            print(e)
            messages.error(request,"an error occured while positioning and listing")
    elif request.method=="GET":
        list_forms=ListingForm()
        location_forms=LocationForm()
    return render(request,'app/list.html',{'list_forms':list_forms,'location_forms':location_forms})

def show_single_item(request,id):
    try:
        single_item=Listing.objects.get(id=id)
        if single_item is None:
            raise Exception
        return render(request,'app/single_item.html',{'single_item':single_item})
    except Exception as e:
        return  messages(request,f"Invalid id provided")
        redirect('login_home')


@login_required
def edit_listing_page(request, id):
    try:

        listing = Listing.objects.get(id=id)

        if not listing:
            raise Exception("Listing not found")

        if request.method == "POST":

            listing_form = ListingForm(request.POST, request.FILES, instance=listing)
            location_form = LocationForm(request.POST, instance=listing.location)

            if listing_form.is_valid() and location_form.is_valid():
                listing_form.save()
                location_form.save()
                messages.info(request, "Updated successfully")
                return redirect('login_home')
            else:
                messages.error(request, "An error occurred")

                return render(request, "app/edit.html", {'listing_form': listing_form, 'location_form': location_form})
        else:

            listing_form = ListingForm(instance=listing)
            location_form = LocationForm(instance=listing.location)


        return render(request, "app/edit.html", {'listing_form': listing_form, 'location_form': location_form})
    except Listing.DoesNotExist:

        messages.error(request, "Invalid ID provided")
        return redirect('home')

@login_required
def like_listing_view(request, id):
    listing = get_object_or_404(Listing, id=id)

    liked_listing, created = LikedListing.objects.get_or_create(
        profile=request.user.profile, listing=listing)

    if not created:
        liked_listing.delete()
    else:
        liked_listing.save()

    return JsonResponse({
        'is_liked_by_user': created,
    })





