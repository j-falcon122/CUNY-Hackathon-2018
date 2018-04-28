from django.db import models


# Create your models here.
class Shelter(models.Model):
    name = models.CharField(max_length=45, blank=False)
    address = models.CharField(max_length=200, blank=False)
    phone = models.CharField(max_length=45, blank=True)
    post_code = models.CharField(max_length=5, blank=True)
    borough = models.CharField(max_length=45)

