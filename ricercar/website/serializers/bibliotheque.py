from ricercar.website.models.bibliotheque import Bibliotheque
from ricercar.website.serializers.localisation import LocalisationSerializer
from rest_framework import serializers

class BibliothequeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Bibliotheque