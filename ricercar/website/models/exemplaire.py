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
        return u"{0}".format(self.cote_exemplaire)

@receiver(post_save, sender=Exemplaire)
def solr_index(sender, instance, created, **kwarg):
    import uuid
    from django.conf import settings
    import solr

    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:website_exemplaire item_id:{0}".format(instance.id))
    if record:
        # the record already exists, so we'll remove the first
        solrconn.delete(record.results[0]['id'])

    exemplaire = instance
    d = {
        'type': 'website_exemplaire',
        'id': str(uuid.uuid4()),
        'item_id':exemplaire.id,
        'cote_exemplaire': exemplaire.cote_exemplaire,
        'localisation':exemplaire.localisation,
        'etat':exemplaire.etat,
        'remarques':exemplaire.remarques,
        'lien_source':exemplaire.lien_source,
        'voix':exemplaire.voix,

    }
    solrconn.add(**d)
    solrconn.commit()

@receiver(post_delete, sender=Exemplaire)
def solr_delete(sender, instance, created, **kwargs):
    from django.conf import settings
    import solr
    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:website_exemplaire item_id:{0}".format(instance.id))
    solrconn.delete(record.results[0]['id'])
    solrconn.commit()