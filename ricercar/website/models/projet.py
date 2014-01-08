from django.db import models

class Projet(models.Model):
    class Meta:
        app_label="website"

    nom_du_projet = models.CharField(max_length=255, blank=True, null=True)
    liens_url = models.URLField(max_length=200,blank=True, null=True)

    def __unicode__(self):
        return u"{0}".format(self.nom_du_projet)
