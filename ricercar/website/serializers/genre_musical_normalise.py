from ricercar.website.models.genre_musical_normalise import GenreMusicalNormalise

from rest_framework import serializers

class GenreMusicalNormaliseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GenreMusicalNormalise