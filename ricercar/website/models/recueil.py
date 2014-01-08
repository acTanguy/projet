from django.db import models


class Recueil(models.Model):
    class Meta:
        app_label="website"

    IMPRIME = 'imp'
    MANUSCRIT = 'ms'
    CHOIX_FORMAT = (
        (MANUSCRIT, 'manuscrit'),
        (IMPRIME, 'imprime'),
    )

    titre = models.CharField(max_length=255, blank=True, null=True)
    titre_traduit = models.CharField(max_length=255, blank=True, null=True)
    catalogue_id = models.ManyToManyField("website.Catalogue", related_name='recueil',blank=True, null=True)
    support = models.CharField(max_length=3, choices=CHOIX_FORMAT, default=IMPRIME)
    ville_edition = models.ForeignKey("website.Localisation", related_name='lieu_d_edition_de',blank=True, null=True)
    datation = models.CharField(max_length=16, blank=True, null=True)
    editeur = models.ForeignKey("website.Personne", related_name='editions', blank=True, null=True)
    compositeurs = models.ForeignKey("website.Personne", blank=True, null=True)
    nombre_pieces = models.IntegerField(max_length=4, blank=True, null=True)
    cahiers = models.IntegerField(max_length=4, blank=True, null=True)
    cahiers_manquants = models.IntegerField(max_length=4, blank=True, null=True)
    genre_musical_normalise = models.ManyToManyField("website.GenreMusicalNormalise", related_name='recueils', blank=True, null=True)
    genre_musical_detaille = models.ManyToManyField("website.GenreMusicalDetaille", related_name='recueils', blank=True, null=True)
    reemission = models.ManyToManyField("self", blank=True, null=True)
    reedition = models.ManyToManyField("self", blank=True, null=True)
    remarques = models.TextField(blank=True, null=True)
    projet = models.ManyToManyField("website.Projet", related_name='dans')

    def __unicode__(self):
        return u"{0}".format(self.titre)
