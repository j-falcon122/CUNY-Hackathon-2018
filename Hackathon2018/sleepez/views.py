from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .templatetags.shelter_tags import * 
from .templatetags.google_maps_tags import * 
from django.conf import settings
from .form import SearchForm, HostForm
from .models import PotentialHost
from .utils import update_shelters


# Create your views here.
def index(request):
    return render(request, 'sleepez/index.html')

def about(request):
    return render(request, 'sleepez/about.html')    

def sign_up(request):
    return render(request, 'sleepez/sign_up.html')


def update(request):
    update_shelters()
    return HttpResponse('Shelters have been updated.')


def google_maps(request):
    # get_geocode()
    get_reverse_geocode()
    return render(request, 'sleepez/google_maps.html')


def show_map(request, origin, destination):
    url = ('https://www.google.com/maps/embed/v1/directions?' +
           'key='+settings.API_KEY +
           '&origin='+origin +
           '&destination=' + destination +
           '&mode=walking&zoom=15'
           )
    context_dict = {
        'url': url,
        'origin': origin,
        'destination':destination,
    }
    return render(request, 'sleepez/search.html', context_dict)


def search_form(request):
    form = SearchForm
    context_dict = {'address_validator': form}
    return render(request,'sleepez/search_form.html', context_dict)


class HostCreateView(SuccessMessageMixin, CreateView):
    model = PotentialHost
    fields = '__all__'
    template_name = 'sleepez/host_form.html'
    success_message = 'Application has been processed. Allow a couple of days for us to review it.'
    success_url = '#'
