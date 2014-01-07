from django.db import models


class Piece(models.Model):
    class Meta:
        app_label="ricercar"

    titre = models.CharField(max_length=255)
    recueil_id = models.ForeignKey("ricercar.website.Recueil", related_name='pieces', blank=True, null=True)
    compositeur = models.ForeignKey("ricercar.website.Personne", related_name='composition', blank=True, null=True)
    poete= models.ForeignKey("ricercar.website.Personne", blank=True, null=True)
    concordance_ms = models.ManyToManyField("self", blank=True, null=True)
    concordance_imp = models.ManyToManyField("self", blank=True, null=True)
    sources = models.URLField(max_length=200,blank=True, null=True)
    nombre_de_voix = models.IntegerField(max_length=4, blank=True, null=True)
    formation = models.CharField(max_length=255)
    nombre_de_voix_manquante = models.IntegerField(max_length=4, blank=True, null=True)
    genre_musical_normalise = models.ManyToManyField("ricercar.website.GenreMusicalNormalise", related_name='pieces', blank=True, null=True)
    genre_musical_detaille = models.ManyToManyField("ricercar.website.GenreMusicalDetaille", related_name='pieces', blank=True, null=True)
    pdf_link = models.URLField(max_length=200,blank=True, null=True)
    mei_Link = models.URLField(max_length=200,blank=True, null=True)
    
    remarques = models.TextField(blank=True, null=True)
