from django.shortcuts import render
from django.views.generic import View
from .models import *

# Create your views here.


class Home(View):
    def get (self, request):
        obj_store = Store.objects.last()
        print (obj_store)

        return render (request, 'index.html', {'obj_store' : obj_store})

     

