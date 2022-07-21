from django.urls import path

from . import views

urlpatterns = [
    path('payment_start', views.payment_start, name='payment_start'),
    path('payment_return', views.payment_return, name='payment_return'),
]
