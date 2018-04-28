from django.contrib import admin
from .models import Shelter, PotentialHost


# Register your models here.
class ShelterAdmin(admin.ModelAdmin):
    list_display = ('name', 'address',)
    search_fields = list_display


class HostAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_phone')
    search_fields = list_display

# models = []
admin.site.register(Shelter,ShelterAdmin)
admin.site.register(PotentialHost, HostAdmin)