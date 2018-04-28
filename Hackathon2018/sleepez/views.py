from django.shortcuts import render
import requests 
import json
from django.http import HttpResponse
from .templatetags.shelter_tags import * 
from .templatetags.google_maps_tags import * 

# Create your views here.
def index(request):
    return render(request, 'sleepez/index.html')

def update(request):
    update_shelters()
    return HttpResponse('Shelters have been updated.')

def google_maps(request):
    # get_geocode()
    get_reverse_geocode()
    return HttpResponse('google_maps')


