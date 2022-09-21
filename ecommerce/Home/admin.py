from email.mime import image
from django.contrib import admin


from Home.views import Home
from .models import * 


#Register your models here.
admin.site.register(Store)

admin.site.register(ImageBanner)

