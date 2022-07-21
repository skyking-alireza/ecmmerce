from datetime import datetime
from django import template
register = template.Library()
@register.filter
def setrequest(value):

    print(value)
    return 1
@register.filter
def is_numberic(value):
    return str(value).isnumeric()
@register.filter
def is_str(value):
    return type(value) is str


