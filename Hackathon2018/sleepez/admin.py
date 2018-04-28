from django.contrib import admin
from .models import Shelter


# Register your models here.
class ShelterAdmin(admin.ModelAdmin):
    list_display = ('name', 'address',)
    search_fields = list_display


admin.site.register(Shelter, ShelterAdmin)