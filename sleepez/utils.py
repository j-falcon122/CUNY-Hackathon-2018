from .models import Shelter
from django.conf import settings
import datetime, json, googlemaps


def open_json(file_path):
    with open(file_path) as f:
        return json.loads(f.read())


def get_geocode(address):
    gmaps = googlemaps.Client(key=settings.MAPS_API_KEY)
    geocode_result = gmaps.geocode(address)
    return geocode_result


def get_geolocation_list():
    shelters = Shelter.objects.all()
    addresses = list()
    for branch in shelters:
        location = {}
        addresses.append([branch.latitude, branch.longitude])
    return addresses


def get_geolocation(address):
    jfile = get_geocode(address)
    latitude = jfile[0]['geometry']['location']['lat']
    longitude = jfile[0]['geometry']['location']['lng']
    return latitude, longitude


# Look up an address with reverse geocoding
def get_reverse_geocode(latitude, longitude):
    gmaps = googlemaps.Client(key=settings.MAPS_API_KEY)
    reverse_geocode_result = gmaps.reverse_geocode((latitude, longitude))
    address = reverse_geocode_result[0]['formatted_address']
    return address


def get_shelter_list(url):
    try:
        # with urllib.request.urlopen(url) as url:
        data = json.loads(open(url))
            # data = json.loads(url.read().decode())
        return data
    except:
        return []


def shelter_exists(provider):
    try:
        name = provider['nta']
        Object = Shelter.objects.get(name=name)
    except Shelter.DoesNotExist:
        return False
    return True


def update_shelters():
    url = 'sleepez/static/data/shelters.json'
    # url = 'https://data.cityofnewyork.us/resource/5ud2-iqje.json'
    shelters = open_json(url)
    for provider in shelters:
        if not shelter_exists(provider):
            new_shelter = Shelter(
                name= provider['nta'],
                address = provider['address'],
                phone = provider['phone_number'],
                latitude = get_geolocation(provider['address'])[0],
                longitude = get_geolocation(provider['address'])[1],
                borough = provider['borough'],
            )
            new_shelter.save()
