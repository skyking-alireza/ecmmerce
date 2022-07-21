from datetime import datetime

import pytz
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

# Create your models here.
from django.urls import reverse



class customers(AbstractUser):
    phone_number = models.CharField(max_length=12 , null=True , blank=True)
    otp = models.CharField(max_length=7, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='profile' , null=True, blank=True)
    colleague = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True,blank=True)
    is_active = models.BooleanField(default=True,blank=True)
class state(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title
    def deleteitem(self):
        return reverse('delete_state', args=[int(self.id)])
class city(models.Model):
    state = models.ForeignKey(state, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title
    def deleteitem(self):
        return reverse('delete_city', args=[int(self.id)])
class cart(models.Model):
    user = models.ForeignKey('account.customers',on_delete=models.CASCADE)
    pri =  models.ForeignKey('product.Variable_price',on_delete=models.DO_NOTHING)
    pro =  models.ForeignKey('product.product',on_delete=models.DO_NOTHING)
    count = models.IntegerField()
class address(models.Model):
    user = models.ForeignKey(customers,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    city = models.ForeignKey(city,on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    zipcode = models.CharField(max_length=10)
    def __str__(self):
        return self.title
class payment(models.Model):
    order_id = models.TextField()
    user = models.ForeignKey(customers, on_delete=models.CASCADE)
    user_address = models.ForeignKey(address, on_delete=models.CASCADE)
    amount = models.CharField(max_length=20)
    payment_id = models.TextField()
    date = models.CharField(max_length=10)
    card_number = models.TextField(default="****")
    idpay_track_id = models.IntegerField(default=0000)
    bank_track_id = models.TextField(default=0000)
    Payment_not_made = 1
    Payment_failed = 2
    An_error_has_occurred = 3
    Reversed_system = 6
    Cancel_payment = 7
    Awaiting_payment_confirmation = 10
    Transaction_verified = 100
    status_choied = (
        (Payment_not_made, 'پرداخت انجام نشده است'),
        (Payment_failed, 'پرداخت ناموفق بوده است'),
        (An_error_has_occurred, 'خطا رخ داده است'),
        (Reversed_system, 'برگشت خورده سیستمی'),
        (Cancel_payment, 'انصراف از پرداخت'),
        (Awaiting_payment_confirmation, 'در انتظار تایید پرداخت'),
        (Transaction_verified, 'تراکنش تایید شده'),
    )
    status = models.IntegerField(choices=status_choied)
    def __str__(self):
        return self.user.get_full_name()
    def get_absulot_url(self):
        return reverse('order_details',args=[str(self.order_id)])
    def returnstatus(self):
        status = {1:'پرداخت انجام نشده است',2:'پرداخت ناموفق بوده است',3:'خطا رخ داده است',6:'برگشت خورده سیستمی',7:'انصراف از پرداخت',10:'در انتظار تایید پرداخت',100:'تراکنش تایید شده'}
        return status[self.status]

class orders(models.Model):
    pro = models.ForeignKey("product.product",on_delete=models.CASCADE )
    user = models.ForeignKey('account.customers',on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.ForeignKey("product.Variable_price",on_delete=models.CASCADE )
    payment_id = models.ForeignKey('account.payment',on_delete=models.CASCADE )
