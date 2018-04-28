from django.shortcuts import render
import requests 
import json
from django.http import HttpResponse
from .templatetags.shelter_tags import * 
from .templatetags.google_maps_tags import * 
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'sleepez/index.html')

def update(request):
    update_shelters()
    return HttpResponse('Shelters have been updated.')

def google_maps(request):
    # get_geocode()
    get_reverse_geocode()
    return render(request, 'sleepez/google_maps.html')

def test(request):
    return render(request, 'sleepez/search.html')

def show_map(request, origin, destination):
    url = ('https://www.google.com/maps/embed/v1/directions?' +
           'key=AIzaSyClUKFNtktLHjlLPKsQIyU7RH0v8TDiTwI' +
           '&origin='+origin +
           '&destination=' + destination +
           '&mode=walking'
           )
    context_dict = {
        'url': url,
        'origin': origin,
        'destination':destination,
    }
    return render(request, 'sleepez/search.html', context_dict)

