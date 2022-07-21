from django.db import models

# Create your models here.
from django.urls import reverse

from gallery.models import images


class logo_site(models.Model):
    image = models.ImageField(upload_to='logo')
    title = models.CharField(max_length=150)
    def __str__(self):
        return self.image.url
class icon_site(models.Model):
    image = models.ImageField(upload_to='icon')
    def __str__(self):
        return self.image.url
class navbar_process(models.Model):
    title = models.CharField(max_length=30)
    image = models.ForeignKey(images,on_delete=models.CASCADE)
    descriptions = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    def itemdelete(self):
        return reverse('delete_navbar_process', args=[int(self.id)])
class swiper(models.Model):
    title = models.CharField(max_length=50)
    image = models.ForeignKey(images, on_delete=models.CASCADE)
    descriptions = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    def itemdelete(self):
        return reverse('delete_swiper', args=[int(self.id)])