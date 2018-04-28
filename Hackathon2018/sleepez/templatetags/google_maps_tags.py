from django import template
import googlemaps
from datetime import datetime
register = template.Library()



def get_geocode():
    gmaps = googlemaps.Client(key='AIzaSyAso1CPfl8yBx56oJI7wVUE0yJL3o_bx0k')    
    # Geocoding an address

    # Hardcoded - CHANGE
    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
    # print geocode_result

    return geocode_result

    # Look up an address with reverse geocoding
def get_reverse_geocode():
    gmaps = googlemaps.Client(key='AIzaSyAso1CPfl8yBx56oJI7wVUE0yJL3o_bx0k')
    reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))


    now = datetime.now()
    print "seee this?"
    directions_result = gmaps.directions("Sydney Town Hall",
                                             "Parramatta, NSW",
                                             mode="driving",
                                             departure_time=now)
    print "how about this?"
    print directions_result
