from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class Exemplaire(models.Model):
    class Meta:
        app_label="website"

    COMPLET = 'CO'
    INCOMPLET = 'IN'
    CHOIX_ETAT =(
        (COMPLET, 'Complet'),
        (INCOMPLET, 'Incomplet'),
    )

    localisation = models.ForeignKey("website.Bibliotheque", blank=True, null=True)
    cote_exemplaire = models.CharField(max_length=16, blank=True, null=True)
    etat = models.CharField(max_length=3, choices=CHOIX_ETAT, default=COMPLET)
    remarques = models.TextField(blank=True, null=True)
    lien_source = models.URLField(max_length=200,blank=True, null=True)
    voix = models.ManyToManyField("website.Voix", related_name='recueil',blank=True, null=True)


    def __unicode__(self):
        return u"{0}".format(self.localisation)

