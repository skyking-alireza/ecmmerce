from django.db import models

# Create your models here.

class images(models.Model):
    image = models.ImageField(upload_to='gallery')
    alt = models.CharField(max_length=150 , null=True , blank=True)
    class Meta:
        ordering = ['-id']