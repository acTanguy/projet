# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Piece'
        db.create_table(u'website_piece', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('titre_normalise', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('recueil_id', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='pieces', null=True, to=orm['website.Recueil'])),
            ('compositeur', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='composition', null=True, to=orm['website.Personne'])),
            ('poete', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Personne'], null=True, blank=True)),
            ('nombre_de_voix', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True, blank=True)),
            ('formation', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('nombre_de_voix_manquantes', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True, blank=True)),
            ('genre_musical_normalise', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='pieces', null=True, to=orm['website.GenreMusicalNormalise'])),
            ('genre_musical_detaille', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='pieces', null=True, to=orm['website.GenreMusicalDetaille'])),
            ('pdf_link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('mei_link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('remarques', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('website', ['Piece'])


    def backwards(self, orm):
        # Deleting model 'Piece'
        db.delete_table(u'website_piece')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'website.article': {
            'Meta': {'object_name': 'Article'},
            'auteur': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'actualites'", 'to': u"orm['auth.User']"}),
            'categorie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Categorie']"}),
            'contenu': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lien': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'website.bibliotheque': {
            'Meta': {'object_name': 'Bibliotheque'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localisation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Localisation']"}),
            'nom_normalise': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'sigle_rism': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'website.catalogue': {
            'Meta': {'object_name': 'Catalogue'},
            'choix_catalogue': ('django.db.models.fields.CharField', [], {'default': "'RISM_A'", 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifiant': ('django.db.models.fields.CharField', [], {'max_length': '32', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        'website.categorie': {
            'Meta': {'object_name': 'Categorie'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'website.exemplaire': {
            'Meta': {'object_name': 'Exemplaire'},
            'cote_exemplaire': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'etat': ('django.db.models.fields.CharField', [], {'default': "'CO'", 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lien_source': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'localisation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Bibliotheque']", 'null': 'True', 'blank': 'True'}),
            'remarques': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'voix': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'recueil'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['website.Voix']"})
        },
        'website.genremusicaldetaille': {
            'Meta': {'object_name': 'GenreMusicalDetaille'},
            'genre_musical': ('django.db.models.fields.CharField', [], {'default': 'None', 'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'website.genremusicalnormalise': {
            'Meta': {'object_name': 'GenreMusicalNormalise'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'provenance': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'style': ('django.db.models.fields.CharField', [], {'default': "'profane'", 'max_length': '128'})
        },
        'website.localisation': {
            'Meta': {'object_name': 'Localisation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom_ville_francais': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'nom_ville_normalise_langue': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'nom_ville_source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pays_francais': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pays_normalise_langue': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'website.personne': {
            'Meta': {'object_name': 'Personne'},
            'bibliographie': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_mort': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'date_naissance': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lieu_activite': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'lieu_d_activite_de'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['website.Localisation']"}),
            'lieu_mort': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'lieu_de_mort_de'", 'null': 'True', 'to': "orm['website.Localisation']"}),
            'lieu_naissance': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'lieu_de_naissance_de'", 'null': 'True', 'to': "orm['website.Localisation']"}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'nom_bref': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'periode_activite': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'remarques': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'role': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'activite_de'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['website.Role']"}),
            'variante_nom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'website.piece': {
            'Meta': {'object_name': 'Piece'},
            'compositeur': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'composition'", 'null': 'True', 'to': "orm['website.Personne']"}),
            'concordance_imp': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'concordance_imp_rel_+'", 'null': 'True', 'to': "orm['website.Piece']"}),
            'concordance_ms': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'concordance_ms_rel_+'", 'null': 'True', 'to': "orm['website.Piece']"}),
            'formation': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'genre_musical_detaille': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'pieces'", 'null': 'True', 'to': "orm['website.GenreMusicalDetaille']"}),
            'genre_musical_normalise': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'pieces'", 'null': 'True', 'to': "orm['website.GenreMusicalNormalise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mei_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'nombre_de_voix': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'nombre_de_voix_manquantes': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'pdf_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'poete': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Personne']", 'null': 'True', 'blank': 'True'}),
            'recueil_id': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'pieces'", 'null': 'True', 'to': "orm['website.Recueil']"}),
            'remarques': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'titre_normalise': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'website.projet': {
            'Meta': {'object_name': 'Projet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'liens_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'nom_du_projet': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        'website.recueil': {
            'Meta': {'object_name': 'Recueil'},
            'catalogue_id': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'recueil'", 'null': 'True', 'to': "orm['website.Catalogue']"}),
            'compositeurs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['website.Personne']", 'null': 'True', 'blank': 'True'}),
            'datation': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'editeur': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editions'", 'null': 'True', 'to': "orm['website.Personne']"}),
            'exemplaire': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'autres_exemplaires'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['website.Exemplaire']"}),
            'genre_musical_detaille': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'recueils'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['website.GenreMusicalDetaille']"}),
            'genre_musical_normalise': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'recueils'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['website.GenreMusicalNormalise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_pieces': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'projet': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'dans'", 'symmetrical': 'False', 'to': "orm['website.Projet']"}),
            'reedition': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'reedition_rel_+'", 'null': 'True', 'to': "orm['website.Recueil']"}),
            'remarques': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'support': ('django.db.models.fields.CharField', [], {'default': "'imp'", 'max_length': '3'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'titre_traduit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ville_edition': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'lieu_d_edition_de'", 'null': 'True', 'to': "orm['website.Localisation']"})
        },
        'website.role': {
            'Meta': {'object_name': 'Role'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'website.voix': {
            'Meta': {'object_name': 'Voix'},
            'abreviation': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'voix': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        }
    }

    complete_apps = ['website']