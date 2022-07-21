from django.urls import path

from main.views import send_forgot_code, view_reset_passwd, setpassword
from .views import *

name_app = "account"
urlpatterns= [
    path("return_code" , return_code , name = "return_code"),
    path("profile" , profile , name = "profile"),
    path("create_account", create_account, name="create_account"),
    path("phone_number_change", change_phone_number, name="phone_number_change"),
    path("change_password", change_password, name="change_password"),
    path("address", manage_address, name="address"),
    path("update_address", update_address, name="update_address"),
    path("orders", manage_orders, name="orders"),
    path("view_login", view_login, name="view_login"),
    path("view_logout", view_logout, name="view_logout"),
    path("reset_code", send_forgot_code, name="reset_code"),
    path("view_reset_passwd", view_reset_passwd, name="view_reset_passwd"),
    path("setpassword", setpassword, name="setpassword"),
    ]