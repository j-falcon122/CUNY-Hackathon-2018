from django import template
from ..models import Shelter
from ..utils import *
import json


register = template.Library()


@register.filter(name='add_class')
def add_class(field, css):
    return field.as_widget(attrs={'class': css})


@register.filter(name='get_item')
def get_item(array, index):
    index = eval(index)
    return array[index]