from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class Piece(models.Model):
    class Meta:
        app_label="website"

    titre = models.CharField(max_length=255)
    recueil_id = models.ForeignKey("website.Recueil", related_name='pieces', blank=True, null=True)
    compositeur = models.ForeignKey("website.Personne", related_name='composition', blank=True, null=True)
    poete= models.ForeignKey("website.Personne", blank=True, null=True)
    concordance_ms = models.ManyToManyField("self", blank=True, null=True)
    concordance_imp = models.ManyToManyField("self", blank=True, null=True)
    nombre_de_voix = models.IntegerField(max_length=4, blank=True, null=True)
    formation = models.CharField(max_length=255, blank=True, null=True)
    nombre_de_voix_manquantes = models.IntegerField(max_length=4, blank=True, null=True)
    genre_musical_normalise = models.ForeignKey("website.GenreMusicalNormalise", related_name='pieces', blank=True, null=True)
    genre_musical_detaille = models.ForeignKey("website.GenreMusicalDetaille", related_name='pieces', blank=True, null=True)
    pdf_link = models.URLField(max_length=200,blank=True, null=True)
    mei_link = models.URLField(max_length=200,blank=True, null=True)

    remarques = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"{0}".format(self.titre)