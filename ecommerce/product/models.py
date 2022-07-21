import time

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
import statistics
from account.models import customers
from gallery.models import images
from jalali_date import datetime2jalali
image_not_found = 76
class maincategory(models.Model):
    name = models.CharField(max_length=150)
    descriptions = models.TextField(max_length=450)
    keywords = models.CharField(max_length=150)
    tags = models.CharField(max_length=150)
    def __str__(self):
        return self.name
class subcategory(models.Model):
    category = models.ForeignKey(maincategory , on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    showindexpage = models.BooleanField(default=0)
    image = models.ForeignKey(images, null=True, on_delete=models.SET_DEFAULT, default=image_not_found)
    descriptions = models.TextField(max_length=450)
    keywords = models.CharField(max_length=150)
    tags = models.CharField(max_length=150)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("product_grid") + '?filter="category":"%s"'% self.id
class treemenu(models.Model):
    name = models.CharField(max_length=150)
    tree = models.BooleanField(default=0)
    link =  models.CharField(max_length=150 , null=True , blank=True)
    def __str__(self):
        return self.name
class menu(models.Model):
    tree = models.ForeignKey(treemenu , on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class submenu(models.Model):
    selectmenu = models.ForeignKey(menu , on_delete=models.CASCADE)
    category = models.ForeignKey(subcategory , on_delete=models.CASCADE)
    def __str__(self):
        return self.category.name
    def get_absolute_url(self):
        return reverse("product_grid") + '?filter="category":"%s"'% self.category.id
class brand(models.Model):
    name = models.CharField(max_length=150)
    showindexpage = models.BooleanField(default=0)
    image = models.ForeignKey(images, null=True, on_delete=models.SET_DEFAULT, default=image_not_found)
    descriptions = models.TextField(max_length=450)
    keywords = models.CharField(max_length=150)
    tags = models.CharField(max_length=150)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("product_grid") + '?filter="brand":"%s"'% self.id
class color(models.Model):
    name = models.CharField(max_length=150)
    color = models.CharField(max_length=10)
    def __str__(self):
        return self.name
class warranty(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name
class details(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name
class valuedetails(models.Model):
    namedetails = models.ForeignKey(details , on_delete=models.CASCADE)
    value = models.CharField(max_length=250)
    class Meta:
        ordering = ['namedetails']
    def __str__(self):
        return self.value

class product(models.Model):
    name = models.CharField(max_length=150 , unique=True )
    engname = models.CharField(max_length=150 , unique=True)
    category = models.ManyToManyField(subcategory)
    weight = models.CharField(max_length=150 , null=True , blank=True)
    dimensions = models.CharField(max_length=150 , null=True , blank=True)
    warranty = models.ForeignKey(warranty , null=True , blank=True , on_delete=models.SET_DEFAULT , default=image_not_found)
    image = models.ForeignKey(images,on_delete=models.SET_DEFAULT, default=image_not_found , related_name='product')
    imageother = models.ManyToManyField(images , related_name='imageother')
    open_sale = 1
    close_sale = 2
    check_inventory = 3
    stop_production = 4
    coming_soon = 5
    status_choied = (
        (open_sale, 'در حال فروش'),
        (close_sale, 'توقف فروش'),
        (check_inventory, 'اتمام موجودی'),
        (stop_production, 'توقف تولید'),
        (coming_soon, 'به زودی موجود می شود'),
    )
    allowcomment = models.BooleanField(default=0)
    visibility = models.BooleanField(default=0)
    status = models.IntegerField(choices=status_choied)
    details = models.ManyToManyField(valuedetails)
    meta_descriptions = models.CharField(max_length=500)
    meta_keywords = models.CharField(max_length=150 )
    descriptions = HTMLField()
    create_at = models.DateTimeField(auto_now_add=True)
    brand = models.ForeignKey(brand ,on_delete=models.SET_DEFAULT , default=1)
    countview = models.IntegerField(default=0)
    class Meta:
        ordering = ['-id']
    def __str__(self):
        return self.name
    def pro_view(self):
        self.countview += 1
        self.save()
    def get_absolute_url(self):
        return reverse('product', args=[int(self.id),str(self.name)])
    def return_cart(self,set,count,idcart):
        return {'name':self.name,'image':self.image.image.url,'url':self.get_absolute_url(),'price':set,'count':count,'idcart':idcart}
    def get_price(self):
        def check_status(x):
            if x[0] == self.status:
                return x[1]
        check_statused = list(filter(check_status, self.status_choied))
        if 1 == self.status:
            queryset = Variable_price.objects.filter(product__id=self.id) or False
            if queryset:
                return queryset.first()
            else:
                return 'بدون قیمت'
        else:
            return check_statused[0][1]
    def get_stars(self):
        comment = comment_product.objects.filter(product_id=self.id, show=True) or False
        if comment:
            return int(statistics.mean(map(lambda x: x.starts, comment))) if comment else False
        else:
            return 'امتیازی ثبت نشده'

class Variable(models.Model):
    name = models.CharField(max_length=150 )
    def __str__(self):
        return self.name
class Variable_price(models.Model):
    product = models.ForeignKey(product , on_delete=models.CASCADE)
    color = models.ForeignKey(color , on_delete=models.CASCADE, null=True)
    details = models.ForeignKey(Variable , on_delete=models.CASCADE, null=True)
    price = models.IntegerField()
    min = models.IntegerField(null=True, blank=True)
    max = models.IntegerField()
    count = models.IntegerField()
    colleague = models.BooleanField(default=0 ,null=True, blank=True)
    price_colleague = models.FloatField(null=True, blank=True)
    min_colleague = models.IntegerField(null=True, blank=True)
    max_colleague = models.IntegerField(null=True, blank=True)
    count_colleague = models.IntegerField(null=True, blank=True)
    discount = models.BooleanField(default=0 ,null=True, blank=True)
    price_discount = models.IntegerField(null=True, blank=True)
    timestart = models.DateTimeField(null=True, blank=True)
    timeend = models.DateTimeField(null=True, blank=True)
    class Meta:
        ordering = ['-discount']
    def jstart(self):
        return datetime2jalali(self.timestart)
    def jend(self):
        return datetime2jalali(self.timeend)
    def checkdate(self):
        try :
            if self.timeend.timestamp() < time.time():
                self.discount = 0
                self.save()
                return 'ok'
            return self.timeend.timestamp()
        except:
            return 'ok'
    def show_price(self,request):
        if self.product.status == 1 or self.count != 0:
            if request.user.colleague:
                if self.price_colleague:
                    return self.price_colleague
                else:
                    if self.price_discount:
                        return self.price_discount
                    else:
                        return self.price
            else:
                if self.price_discount:
                    return self.price_discount
                else:
                    return self.price
        else:
            return 'ناموجود'
class comment_product(models.Model):
    account = models.ForeignKey(customers , on_delete=models.CASCADE)
    product = models.ForeignKey(product , on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    starts = models.IntegerField()
    text = models.TextField(max_length=1024)
    show = models.BooleanField(default=False)
    sendtime = models.CharField(max_length=15)
    def __str__(self):
        return self.title
