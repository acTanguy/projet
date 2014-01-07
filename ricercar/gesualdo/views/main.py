from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import JSONRenderer, XMLRenderer
from rest_framework import permissions
from ricercar.website.models.recueil import Recueil

def home(request):

    recueils = Recueil.objects.all()
    return render(request, "accueil.html", {"recueils":recueils})

