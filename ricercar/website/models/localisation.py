from django.db import models

class Localisation(models.Model):
    class Meta:
        app_label="ricercar"

    pays_francais = models.CharField(max_length=255)
    pays_normalise_langue = models.CharField(max_length=255)
    nom_ville_normalise_langue = models.CharField(max_length=255, blank=True, null=True)
    nom_ville_francais = models.CharField(max_length=255, blank=True, null=True)
    nom_ville_source = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u"{0}, ({1})".format(self.pays_normalise_langue, self.nom_ville_normalise_langue)