from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import JSONRenderer, XMLRenderer
from rest_framework import permissions
from ricercar.website.models.blog import Article

def home(request):

    articles = Article.objects.all()
    return render(request, "index.html", {'derniers_articles':articles})

def projets(request):
    return render(request, "main/projets.html")
