from django.db import models
from ricercar.website.models.localisation import Localisation

class Bibliotheque(models.Model):
    class Meta:
        app_label="website"

    nom_normalise = models.CharField(max_length=255, blank=True, null=True)
    localisation = models.ForeignKey("Localisation")
    sigle_rism = models.CharField(max_length=255, blank=True, null=True)


    def __unicode__(self):
        return u"{0} / {1}. {02}".format(self.sigle_rism, self.localisation, self.nom_normalise)