from django.conf import settings
from django.urls import path, re_path

import account.views
import product.views
from main import views
name_app = "main"
urlpatterns= [
    path("" , views.index , name = "index"),
    path("return_header" , views.return_header , name = "return_header"),
    path("return_footer" , views.return_footer , name = "return_footer"),
    path("blog-list" , views.blog_list , name = "blog-list"),
    path("search" , views.search , name = "search"),
    path("findimage" , views.set_image , name = "findimage"),
    re_path(r'product/(?P<proid>[-\w]+)/(?P<proname>[-\w]+)', product.views.product__, name="product"),
    path('comment/', product.views.product_comment, name="product_comment"),
    path('add_to_cart', product.views.add_to_cart, name="add_to_cart"),
    path('low_to_cart', product.views.low_to_cart, name="low_to_cart"),
    path('remove_to_cart', product.views.remove_to_cart, name="remove_to_cart"),
    re_path(r'get_data_cart', product.views.get_data_cart, name="get_data_cart"),
    re_path(r'product_grid/$', product.views.product_grid, name="product_grid"),
    re_path(r'page/(?P<pagename>[-\w]+)', views.page_show , name="page_show"),
    re_path(r'blog/(?P<title>[-\w]+)', views.blog, name="blog"),
    path("e404", product.views.e404, name="e404"),
]


