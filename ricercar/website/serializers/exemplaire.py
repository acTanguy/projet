from ricercar.website.models.exemplaire import Exemplaire

from rest_framework import serializers

class ExemplaireSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Exemplaire