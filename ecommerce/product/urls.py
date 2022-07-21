from django.conf import settings
from django.urls import path
from product import views
name_app = "product"
urlpatterns= [
    path("maincategory" , views.maincategory , name = "maincategory"),

]