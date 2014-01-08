from ricercar.website.models.projet import Projet

from rest_framework import serializers

class ProjetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Projet