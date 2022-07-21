from django.contrib import admin
from .models import customers, address

# Register your models here.
admin.site.register([customers,address])