from ricercar.website.models.voix import Voix

from rest_framework import serializers

class VoixSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Voix