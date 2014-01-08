from django.db import models
from django.contrib.auth.models import User



class Categorie(models.Model):
    class Meta:
        app_label="website"

    nom = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nom

class Article(models.Model):
    class Meta:
        app_label="website"

    titre = models.CharField(max_length=100)
    auteur = models.ForeignKey(User, related_name="actualites")

    contenu = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    lien = models.URLField(max_length=200,blank=True, null=True)
    categorie = models.ForeignKey(Categorie)

    def __unicode__(self):
        return u"{} ({} {})".format(self.titre,self.auteur,self.date)




