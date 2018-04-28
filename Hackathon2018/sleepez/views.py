from django.shortcuts import render
import requests 
import json

# Create your views here.
def index(request):
    return render(request, 'sleepez/index.html')


def test(request):
    # response = requests.get('https://data.cityofnewyork.us/resource/5ud2-iqje.json')
    shelters_data = json.load(open('sleepez/static/data/shelters.json'))
    shelters = {}

    for shelter_data in shelters_data:
        area = shelter_data["service_area"]
        address = shelter_data['address']
        shelters[area] = address

    return render(request, 'sleepez/test.html', 
        shelters
        )

