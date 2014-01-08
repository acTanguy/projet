from ricercar.website.models.catalogue import Catalogue
from rest_framework import serializers

class CatalogueSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Catalogue