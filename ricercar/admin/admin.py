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
from ricercar.website.models.exemplaire import Exemplaire
from ricercar.website.models.voix import Voix

class LocalisationAdmin(ModelAdmin):
    pass

class BibliothequeAdmin(ModelAdmin):
    pass

class RoleAdmin(ModelAdmin):
    pass

class PersonneAdmin(ModelAdmin):
    pass

class ArticleAdmin(ModelAdmin):
    pass

class CategorieAdmin(ModelAdmin):
    pass

class ReceuilAdmin(ModelAdmin):
    pass

class ProjetAdmin(ModelAdmin):
    pass

class GenreMusicalNormaliseAdmin(ModelAdmin):
    pass

class ExemplaireAdmin(ModelAdmin):
    filter_horizontal=('voix',)

class VoixAdmin(ModelAdmin):
    pass

site.register(Localisation, LocalisationAdmin)
site.register(Bibliotheque, BibliothequeAdmin)
site.register(Role, RoleAdmin)
site.register(Personne, PersonneAdmin)
site.register(Article, ArticleAdmin)
site.register(Categorie, CategorieAdmin)
site.register(Recueil, ReceuilAdmin)
site.register(Projet, ProjetAdmin)
site.register(GenreMusicalNormalise, GenreMusicalNormaliseAdmin)
site.register(Exemplaire, ExemplaireAdmin)
site.register(Voix, VoixAdmin)