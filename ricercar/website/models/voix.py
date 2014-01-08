from django.db import models


class Voix(models.Model):
    class Meta:
        app_label="website"


    SUPERIUS = 'Superius'
    CANTUS ='Cantus'
    ALTUS ='Altus'
    CONTRATENOR ='Contratenor'
    TENOR ='Tenor'
    BASSUS ='Bassus'
    QUINTUS ='Quintus'
    SEPTIMUS ='Septimus'
    OCTAVUS ='Octavus'
    NONUS ='Nonus'
    CONTIUO ='Continuo'
    DISCANTUS ='Discantus'
    CHOIX_VOIX = (
        (SUPERIUS, 'Superius'),
        (CANTUS, 'Cantus'),
        (ALTUS, 'Altus'),
        (CONTRATENOR, 'Contratenor'),
        (TENOR, 'Tenor'),
        (BASSUS, 'Bassus'),
        (QUINTUS, 'Quintus'),
        (SEPTIMUS, 'Septimus'),
        (OCTAVUS, 'Octavus'),
        (NONUS, 'Nonus'),
        (CONTIUO, 'Continuo'),
        (DISCANTUS, 'Discantus'),
    )

    voix =  models.CharField(max_length=128, choices=CHOIX_VOIX, default=CANTUS)

    def __unicode__(self):
        return u"{0}".format(self.voix)