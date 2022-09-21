from distutils.command.upload import upload
import email
from email.headerregistry import Address
from tkinter import CASCADE
from unicodedata import name
from django.db import models
from django.conf import settings
# Create your models here.

class Store(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(max_length=250, default= '')
    resumen = models.TextField(default= '')
    logo = models.ImageField(upload_to ='store/')
    email =models.EmailField() 
    Address = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    facebook_url = models.URLField(max_length=250)
    instagram_url = models.URLField(max_length=250)

    def __str__(self): 
        return f'{self.user} - {self.name}'

class ImageBanner(models.Model):
        banner = models.ImageField(upload_to ='banner/')
        Store = models.ForeignKey('Store', on_delete=models.CASCADE)

        def __str__(self):
          return f'{self.Store} - {self.banner}'
