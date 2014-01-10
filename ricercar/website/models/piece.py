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
    formation = models.CharField(max_length=255)
    nombre_de_voix_manquantes = models.IntegerField(max_length=4, blank=True, null=True)
    genre_musical_normalise = models.ManyToManyField("website.GenreMusicalNormalise", related_name='pieces', blank=True, null=True)
    genre_musical_detaille = models.ManyToManyField("website.GenreMusicalDetaille", related_name='pieces', blank=True, null=True)
    pdf_link = models.URLField(max_length=200,blank=True, null=True)
    mei_link = models.URLField(max_length=200,blank=True, null=True)

    remarques = models.TextField(blank=True, null=True)

@receiver(post_save, sender=Piece)
def solr_index(sender, instance, created, **kwarg):
    import uuid
    from django.conf import settings
    import solr

    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:website_piece item_id:{0}".format(instance.id))
    if record:
        # the record already exists, so we'll remove the first
        solrconn.delete(record.results[0]['id'])

    piece = instance
    d = {
        'type': 'website_piece',
        'id': str(uuid.uuid4()),
        'item_id':piece.id,
        'titre':piece.titre,
        'recueil_id':piece.recueil_id,
        'recueil_titre':piece.recueil_id.titre,
        'compositeur':piece.compositeur,
        'poete':piece.poete,
        'concordance_imp':piece.concordance_imp,
        'concordance_ms':piece.concordance_ms,
        'nombre_de_voix':piece.nombre_de_voix,
        'formation':piece.formation,
        'nombre_de_voix_manquantes':piece.nombre_de_voix_manquantes,
        'genre_musical_normalise':piece.genre_musical_normalise,
        'genre_musical_detaille':piece.genre_musical_detaille,
        'pdf_link':piece.pdf_link,
        'mei_link':piece.mei_link,

    }
    solrconn.add(**d)
    solrconn.commit()

@receiver(post_delete, sender=Piece)
def solr_delete(sender, instance, created, **kwargs):
    from django.conf import settings
    import solr
    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:website_piece item_id:{0}".format(instance.id))
    solrconn.delete(record.results[0]['id'])
    solrconn.commit()