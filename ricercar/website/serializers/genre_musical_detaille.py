from ricercar.website.models.genre_musical_detaille import GenreMusicalDetaille

from rest_framework import serializers

class GenreMusicalDetailleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GenreMusicalDetaille