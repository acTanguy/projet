from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import JSONRenderer, XMLRenderer
from rest_framework import permissions
from ricercar.website.models.recueil import Recueil
from ricercar.website.models.projet import Projet
from ricercar.website.models.genre_musical_normalise import GenreMusicalNormalise

def home(request):

    projet_model = Projet.objects.filter(nom_du_projet='gesualdo')
    genre = GenreMusicalNormalise.objects.filter(style='profane')
    gesualdo_recueil = Recueil.objects.filter(projet=projet_model).filter(genre_musical_normalise=genre)

    return render(request, "gesualdo_accueil.html", {"gesualdo_recueil":gesualdo_recueil})


