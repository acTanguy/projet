from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class Personne(models.Model):
    class Meta:
        app_label="website"

    nom = models.CharField(max_length=255, blank=True, null=True)
    prenom = models.CharField(max_length=255, blank=True, null=True)
    variante_nom = models.CharField(max_length=255, blank=True, null=True)
    nom_bref = models.CharField(max_length=255, blank=True, null=True)
    date_naissance = models.CharField(max_length=16, blank=True, null=True)
    lieu_naissance = models.ForeignKey("website.Localisation", related_name='lieu_de_naissance_de', blank=True, null=True)
    date_mort = models.CharField(max_length=16, blank=True, null=True)
    lieu_mort  = models.ForeignKey("website.Localisation", related_name='lieu_de_mort_de', blank=True, null=True)
    role = models.ManyToManyField("website.Role", blank=True, null=True, related_name='activite_de')
    lieu_activite = models.ManyToManyField("website.Localisation", related_name='lieu_d_activite_de', blank=True, null=True)
    periode_activite = models.CharField(max_length=16, blank=True, null=True)

    bibliographie = models.TextField(blank=True, null=True)
    remarques = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"{0}, ({1})".format(self.nom, self.prenom)

@receiver(post_save, sender=Personne)
def solr_index(sender, instance, created, **kwarg):
    import uuid
    from django.conf import settings
    import solr

    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:website_personne item_id:{0}".format(instance.id))
    if record:
        # the record already exists, so we'll remove the first
        solrconn.delete(record.results[0]['id'])

    personne = instance
    d = {
        'type': 'website_personne',
        'id': str(uuid.uuid4()),
        'item_id':personne.id,
        'nom' :personne.nom,
        'prenom':personne.prenom,
        'variante_nom':personne.variante_nom,
        'nom_bref':personne.nom_bref,

    }
    solrconn.add(**d)
    solrconn.commit()

@receiver(post_delete, sender=Personne)
def solr_delete(sender, instance, created, **kwargs):
    from django.conf import settings
    import solr
    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:website_personne item_id:{0}".format(instance.id))
    solrconn.delete(record.results[0]['id'])
    solrconn.commit()
