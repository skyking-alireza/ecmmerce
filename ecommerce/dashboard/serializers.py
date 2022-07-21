from rest_framework import serializers
from main.models import logo_site
class return_data_logo(serializers.ModelSerializer):
    class Meta:
        model = logo_site
        fields = '__all__'