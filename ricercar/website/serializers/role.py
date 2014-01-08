from ricercar.website.models.role import Role

from rest_framework import serializers

class RoleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Role