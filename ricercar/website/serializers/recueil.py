from ricercar.website.models.recueil import Recueil

from rest_framework import serializers

class RecueilSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Recueil