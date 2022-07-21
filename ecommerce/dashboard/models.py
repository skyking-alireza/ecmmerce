from django.db import models
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.text import slugify
from tinymce.models import HTMLField

from gallery.models import images
# Create your models here.
image_not_found = 76
class category_blog(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    def deleteitem(self):
        return reverse('delete_category_blogs', args=[int(self.id)])
    def get_absolute_url(self):
        return reverse("blog-list") + '?filter="category":"%s"'% self.id
class page_generator(models.Model):
    title = models.CharField(unique=True,max_length=250)
    url = models.SlugField(unique=True,max_length=250,allow_unicode=True)
    description_seo = models.TextField(max_length=450)
    keywords_seo = models.CharField(max_length=150)
    tags_seo = models.CharField(max_length=150)
    image = models.ForeignKey(images, null=True, on_delete=models.SET_DEFAULT, default=image_not_found)
    text = HTMLField()
    def deleteitem(self):
        return reverse('delete_page', args=[int(self.id)])
    def get_absolute_url(self):
        return reverse('page_show', args=[str(self.url)])
class main_footer(models.Model):
    title = models.CharField(unique=True,max_length=250)
    def __str__(self):
        return self.title
    def deleteitem(self):
        return reverse('delete_footer', args=[int(self.id)])
class sub_footer(models.Model):
    main = models.ForeignKey(main_footer , on_delete=models.CASCADE)
    title = models.CharField(unique=True,max_length=250)
    link = models.CharField(max_length=450)
    def __str__(self):
        return self.title
    def deleteitem(self):
        return reverse('delete_sub_footer', args=[int(self.id)])
class blogs(models.Model):
    title = models.CharField(unique=True,max_length=250)
    category = models.ForeignKey(category_blog,on_delete=models.CASCADE)
    url = models.SlugField(unique=True,max_length=250,allow_unicode=True)
    description_seo = models.TextField(max_length=450)
    keywords_seo = models.CharField(max_length=150)
    tags_seo = models.CharField(max_length=150)
    image = models.ForeignKey(images, null=True, on_delete=models.SET_DEFAULT, default=image_not_found)
    text = HTMLField()
    def deleteitem(self):
        return reverse('delete_blogs', args=[int(self.id)])
    def get_absolute_url(self):
        return reverse('blog', args=[str(self.url)])
class viewsite(models.Model):
    count = models.IntegerField()
    def addview(self):
        self.count += 1
        self.save()