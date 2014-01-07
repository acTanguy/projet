from django.db import models

class GenreMusicalDetaille(models.Model):
    class Meta:
        app_label="ricercar"

    genre_musical = models.CharField(max_length=255)
    ##maybe other thing


    def __unicode__(self):
        return u"{0}".format(self.genre_musical)