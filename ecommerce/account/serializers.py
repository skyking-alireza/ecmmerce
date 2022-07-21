from rest_framework import serializers
from .models import payment
class return_data_payment(serializers.ModelSerializer):
    class Meta:
        model = payment
        fields = '__all__'