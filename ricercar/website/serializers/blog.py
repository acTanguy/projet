from ricercar.website.models.blog import Article, Categorie

from rest_framework import serializers

class CategorieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Categorie

class ArticleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Categorie