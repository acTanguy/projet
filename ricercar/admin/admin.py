from django.contrib.admin import site, ModelAdmin
from ricercar.website.models.localisation import Localisation
from ricercar.website.models.bibliotheque import Bibliotheque
from ricercar.website.models.role import Role
from ricercar.website.models.personne import Personne
from ricercar.website.models.blog import Article
from ricercar.website.models.blog import Categorie
from ricercar.website.models.recueil import Recueil
from ricercar.website.models.projet import Projet
from ricercar.website.models.genre_musical_normalise import GenreMusicalNormalise
from ricercar.website.models.genre_musical_detaille import GenreMusicalDetaille
from ricercar.website.models.exemplaire import Exemplaire
from ricercar.website.models.voix import Voix
from ricercar.website.models.catalogue import Catalogue
from ricercar.website.models.piece import Piece

def reindex_in_solr(modeladmin, request, queryset):
    for item in queryset:
        item.save()
reindex_in_solr.short_description = "Reindexer les objets selectionnes"

class LocalisationAdmin(ModelAdmin):
    actions = [reindex_in_solr]

class BibliothequeAdmin(ModelAdmin):
    actions = [reindex_in_solr]

class RoleAdmin(ModelAdmin):
    actions = [reindex_in_solr]

class PersonneAdmin(ModelAdmin):
    actions = [reindex_in_solr]

class ArticleAdmin(ModelAdmin):
    actions = [reindex_in_solr]

class CategorieAdmin(ModelAdmin):
    actions = [reindex_in_solr]

class ReceuilAdmin(ModelAdmin):
    list_display = ('catalogue_id', 'titre')
    filter_horizontal=('compositeurs', 'genre_musical_normalise', 'genre_musical_detaille', 'projet', 'reedition', 'exemplaire')
    actions = [reindex_in_solr]

class ProjetAdmin(ModelAdmin):
    actions = [reindex_in_solr]

class PieceAdmin(ModelAdmin):
    filter_horizontal=('concordance_ms', 'concordance_imp', )
    actions = [reindex_in_solr]

class GenreMusicalNormaliseAdmin(ModelAdmin):
    actions = [reindex_in_solr]

class GenreMusicalDetailleAdmin(ModelAdmin):
    actions = [reindex_in_solr]

class ExemplaireAdmin(ModelAdmin):
    list_display = ('localisation','etat')
    filter_horizontal=('voix',)
    actions = [reindex_in_solr]

class VoixAdmin(ModelAdmin):
    actions = [reindex_in_solr]

class CatalogueAdmin(ModelAdmin):
    actions = [reindex_in_solr]

site.register(Localisation, LocalisationAdmin)
site.register(Bibliotheque, BibliothequeAdmin)
site.register(Role, RoleAdmin)
site.register(Personne, PersonneAdmin)
site.register(Article, ArticleAdmin)
site.register(Categorie, CategorieAdmin)
site.register(Recueil, ReceuilAdmin)
site.register(Projet, ProjetAdmin)
site.register(GenreMusicalNormalise, GenreMusicalNormaliseAdmin)
site.register(GenreMusicalDetaille, GenreMusicalDetailleAdmin)
site.register(Exemplaire, ExemplaireAdmin)
site.register(Voix, VoixAdmin)
site.register(Catalogue, CatalogueAdmin)
site.register(Piece, PieceAdmin)