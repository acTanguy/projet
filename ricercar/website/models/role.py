from django.db import models

class Role(models.Model):
    class Meta:
        app_label="website"

    role = models.CharField(max_length=255)

    def __unicode__(self):
        return u"{0}".format(self.role)