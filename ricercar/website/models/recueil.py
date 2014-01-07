from django.db import models


class Recueil(models.Model):
    class Meta:
        app_label="ricercar"

    IMPRIME = 'imp'
    MANUSCRIT = 'ms'
    CHOIX_FORMAT = (
        (MANUSCRIT, 'manuscrit'),
        (IMPRIME, 'imprime'),
    )

    titre = models.CharField(max_length=255, blank=True, null=True)
    catalogue_id = models.ManyToManyField("ricercar.website.Catalogue", related_name='recueil',blank=True, null=True)
    support = models.CharField(max_length=3, choices=CHOIX_FORMAT, default=IMPRIME)
    ville_edition = models.ForeignKey("ricercar.website.Localisation", related_name='lieu_d_edition_de',blank=True, null=True)
    datation = models.CharField(max_length=16, blank=True, null=True)
    editeur = models.ForeignKey("ricercar.website.Personne", related_name='editions', blank=True, null=True)
    compositeurs = models.ForeignKey("ricercar.website.Personne", blank=True, null=True)
    localisation = models.ForeignKey("ricercar.website.Bibliotheque", blank=True, null=True)
    nombre_pieces = models.IntegerField(max_length=4, blank=True, null=True)
    cahiers = models.IntegerField(max_length=4, blank=True, null=True)
    cahiers_manquants = models.IntegerField(max_length=4, blank=True, null=True)
    genre_musical_normalise = models.ManyToManyField("ricercar.website.GenreMusicalNormalise", related_name='recueils', blank=True, null=True)
    genre_musical_detaille = models.ManyToManyField("ricercar.website.GenreMusicalDetaille", related_name='recueils', blank=True, null=True)
    cote_exemplaire = models.CharField(max_length=16, blank=True, null=True)
    lien_url = models.URLField(max_length=200,blank=True, null=True)
    reedition = models.ManyToManyField("self", blank=True, null=True)
    remarques = models.TextField(blank=True, null=True)
    projet = models.ManyToManyField("ricercar.website.Projet", related_name='dans')

    def __unicode__(self):
        return u"{0}".format(self.titre)
