from ricercar.website.models.personne import Personne

from rest_framework import serializers

class PersonneSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Personne