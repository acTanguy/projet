from django.db import models
from ricercar.website.models.localisation import Localisation

class GenreMusicalNormalise(models.Model):
    class Meta:
        app_label="website"

    PROFANE = 'profane'
    RELIGIEUX = 'religieux'

    CHOIX_STYLE = (
        (PROFANE, 'Profane'),
        (RELIGIEUX, 'Religieux'),
    )

    style = models.CharField(max_length=128, choices=CHOIX_STYLE, default=PROFANE)
    provenance = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u"{0}, ({1})".format(self.style, self.provenance)
