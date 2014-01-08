from django.db import models

class GenreMusicalDetaille(models.Model):
    class Meta:
        app_label="website"

    MADRIGAL = 'MA'
    MOTET = 'MO'
    MESSE = 'ME'
    CANZONE = 'CA'
    CANTATE = 'CT'
    CHANSON = 'CH'

    CHOIX_GENRE = (
        (MADRIGAL, 'Madrigal'),
        (MOTET, 'Motet'),
        (MESSE, 'Messe'),
        (CANZONE, 'Canzone'),
        (CANTATE, 'Cantate'),
        (CHANSON, 'Chanson'),
    )

    genre_musical = models.CharField(max_length=255, choices=CHOIX_GENRE, default=None)

    def __unicode__(self):
        return u"{0}".format(self.genre_musical)