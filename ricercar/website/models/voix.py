from django.db import models


class Voix(models.Model):
    class Meta:
        app_label="website"
        verbose_name ="Voix"
        verbose_name_plural = "Voix"


    voix =  models.CharField(max_length=128, unique=True)
    abreviation = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return u"{0}".format(self.voix)