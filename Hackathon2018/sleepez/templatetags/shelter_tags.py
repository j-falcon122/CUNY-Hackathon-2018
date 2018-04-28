from django import template
import urllib.request, json
from  ..models import Shelter

register = template.Library()


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

	
@register.filter(name='get_shelters')
def update_shelters():
    url = 'sleepez/static/data/shelters.json'
    # url = 'https://data.cityofnewyork.us/resource/5ud2-iqje.json'
    with open(url) as f:
        shelters = json.loads(f.read())
    # shelters = get_shelter_list(url)

    for provider in shelters:
        if not shelter_exists(provider):
            print("File was read, creating new shelter.'")
            new_shelter = Shelter(
                name= provider['nta'],
                address = provider['address'],
                phone = provider['phone_number'],
                # post_code = provider['postcode'],
                borough = provider['borough'],
            )
            new_shelter.save()
    return None