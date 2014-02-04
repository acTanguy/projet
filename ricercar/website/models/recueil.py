from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class Recueil(models.Model):
    class Meta:
        app_label="website"
        verbose_name = "Recueil"
        verbose_name_plural = "Recueils"

    IMPRIME = 'imp'
    MANUSCRIT = 'ms'
    CHOIX_FORMAT = (
        (MANUSCRIT, 'manuscrit'),
        (IMPRIME, 'imprime'),
    )

    titre = models.CharField(max_length=255, blank=True, null=True)
    titre_traduit = models.CharField(max_length=255, blank=True, null=True)
    catalogue_id = models.ForeignKey("website.Catalogue", related_name='recueil',blank=True, null=True)
    support = models.CharField(max_length=3, choices=CHOIX_FORMAT, default=IMPRIME)
    ville_edition = models.ForeignKey("website.Localisation", related_name='lieu_d_edition_de',blank=True, null=True)
    datation = models.IntegerField(max_length=4, blank=True, null=True)
    editeur = models.ForeignKey("website.Personne", related_name='editions', blank=True, null=True)
    compositeurs = models.ManyToManyField("website.Personne", blank=True, null=True)
    nombre_pieces = models.IntegerField(max_length=4, blank=True, null=True)
    genre_musical_normalise = models.ManyToManyField("website.GenreMusicalNormalise", related_name='recueils', blank=True, null=True)
    genre_musical_detaille = models.ManyToManyField("website.GenreMusicalDetaille", related_name='recueils', blank=True, null=True)
    reedition = models.ManyToManyField("self", blank=True, null=True)
    remarques = models.TextField(blank=True, null=True)
    projet = models.ManyToManyField("website.Projet", related_name='dans')
    exemplaire = models.ManyToManyField("website.Exemplaire", related_name='autres_exemplaires', blank=True, null=True)

    def __unicode__(self):
        return u"{0}".format(self.catalogue_id)

@receiver(post_save, sender=Recueil)
def solr_index(sender, instance, created, **kwarg):
    import uuid
    from django.conf import settings
    import solr


    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:website_recueil item_id:{0}".format(instance.id))
    if record:
        # the record already exists, so we'll remove the first
        solrconn.delete(record.results[0]['id'])

    recueil = instance

    catalogueidentifiant = ""
    if recueil.catalogue_id.choix_catalogue != "":
        catalogueidentifiant = u"{0}, {1}".format(recueil.catalogue_id.choix_catalogue, recueil.catalogue_id.identifiant)
    else:
        catalogueidentifiant = u"{0}".format(recueil.catalogue_id.identifiant)

    ville = ""
    if recueil.ville_edition.nom_ville_normalise_langue !="":
        ville = u"{0}, ({1})".format(recueil.ville_edition.nom_ville_normalise_langue, recueil.ville_edition.pays_normalise_langue)
    else:
        ville = u"{0}".format(recueil.ville_edition.pays_normalise_langue)

    projetnom = u"{0}".format(recueil.projet.all().values_list('nom_du_projet'))


    d = {
        'type': 'website_recueil',
        'id': str(uuid.uuid4()),
        'item_id':recueil.id,
        'titre':recueil.titre,
        'titre_traduit':recueil.titre_traduit,
        'support':recueil.support,
        'datation':recueil.datation,
        'compositeurs':recueil.compositeurs.all().values_list('nom'),
        'nombre_pieces':recueil.nombre_pieces,
        'remarques':recueil.remarques,
        'catalogue':catalogueidentifiant,
        'ville_edition':ville,
        'projet':projetnom,


    }
    solrconn.add(**d)
    solrconn.commit()


@receiver(post_delete, sender=Recueil)
def solr_delete(sender, instance, created, **kwargs):
    from django.conf import settings
    import solr
    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:website_recueil item_id:{0}".format(instance.id))
    solrconn.delete(record.results[0]['id'])
    solrconn.commit()

