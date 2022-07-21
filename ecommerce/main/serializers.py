from rest_framework import serializers

from dashboard.models import sub_footer, main_footer
from main.models import logo_site, icon_site
from product.models import treemenu, menu, submenu, product, subcategory


class return_data_logo(serializers.ModelSerializer):
    class Meta:
        model = logo_site
        fields = '__all__'
class return_data_icon(serializers.ModelSerializer):
    class Meta:
        model = icon_site
        fields = '__all__'
class return_data_treemenu(serializers.ModelSerializer):
    class Meta:
        model = treemenu
        fields = '__all__'
class return_data_menu(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = '__all__'

class return_data_submenu(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name',
    )
    class Meta:
        model = submenu
        fields = '__all__'
class return_data_subcategory(serializers.ModelSerializer):
    class Meta:
        model = subcategory
        fields = '__all__'
class return_data_subfooter(serializers.ModelSerializer):
    class Meta:
        model = sub_footer
        fields = '__all__'
class return_data_mainfooter(serializers.ModelSerializer):
    class Meta:
        model = main_footer
        fields = '__all__'
class return_product(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
    )
    class Meta:
        model = product
        fields = ('category','name','id','image')