from django.contrib import admin
from product.models import *
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'order_link') # notice the order_link !!
admin.site.register([maincategory , subcategory , treemenu , brand , menu , submenu , product , Variable_price , Variable , comment_product])
# Register your models here.
