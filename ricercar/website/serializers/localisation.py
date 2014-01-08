from ricercar.website.models.localisation import Localisation

from rest_framework import serializers

class LocalisationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Localisation