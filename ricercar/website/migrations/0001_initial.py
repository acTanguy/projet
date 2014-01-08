# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Localisation'
        db.create_table(u'website_localisation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pays_francais', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('pays_normalise_langue', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nom_ville_normalise_langue', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('nom_ville_francais', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('nom_ville_source', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('website', ['Localisation'])

        # Adding model 'Bibliotheque'
        db.create_table(u'website_bibliotheque', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom_normalise', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('localisation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Localisation'])),
            ('sigle_rism', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('website', ['Bibliotheque'])

        # Adding model 'Role'
        db.create_table(u'website_role', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('website', ['Role'])

        # Adding model 'Personne'
        db.create_table(u'website_personne', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('prenom', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('variante_nom', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('nom_bref', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('date_naissance', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('lieu_naissance', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='lieu_de_naissance_de', null=True, to=orm['website.Localisation'])),
            ('date_mort', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('lieu_mort', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='lieu_de_mort_de', null=True, to=orm['website.Localisation'])),
            ('periode_activite', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('bibliographie', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('remarques', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('website', ['Personne'])

        # Adding M2M table for field role on 'Personne'
        m2m_table_name = db.shorten_name(u'website_personne_role')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('personne', models.ForeignKey(orm['website.personne'], null=False)),
            ('role', models.ForeignKey(orm['website.role'], null=False))
        ))
        db.create_unique(m2m_table_name, ['personne_id', 'role_id'])

        # Adding M2M table for field lieu_activite on 'Personne'
        m2m_table_name = db.shorten_name(u'website_personne_lieu_activite')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('personne', models.ForeignKey(orm['website.personne'], null=False)),
            ('localisation', models.ForeignKey(orm['website.localisation'], null=False))
        ))
        db.create_unique(m2m_table_name, ['personne_id', 'localisation_id'])

        # Adding model 'GenreMusicalDetaille'
        db.create_table(u'website_genremusicaldetaille', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('genre_musical', self.gf('django.db.models.fields.CharField')(default=None, max_length=255)),
        ))
        db.send_create_signal('website', ['GenreMusicalDetaille'])

        # Adding model 'Catalogue'
        db.create_table(u'website_catalogue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('choix_catalogue', self.gf('django.db.models.fields.CharField')(default='RA', max_length=2)),
            ('identifiant', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
        ))
        db.send_create_signal('website', ['Catalogue'])

        # Adding model 'Piece'
        db.create_table(u'website_piece', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('recueil_id', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='pieces', null=True, to=orm['website.Recueil'])),
            ('compositeur', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='composition', null=True, to=orm['website.Personne'])),
            ('poete', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Personne'], null=True, blank=True)),
            ('nombre_de_voix', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True, blank=True)),
            ('formation', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nombre_de_voix_manquante', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True, blank=True)),
            ('pdf_link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('mei_link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('remarques', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('website', ['Piece'])

        # Adding M2M table for field concordance_ms on 'Piece'
        m2m_table_name = db.shorten_name(u'website_piece_concordance_ms')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_piece', models.ForeignKey(orm['website.piece'], null=False)),
            ('to_piece', models.ForeignKey(orm['website.piece'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_piece_id', 'to_piece_id'])

        # Adding M2M table for field concordance_imp on 'Piece'
        m2m_table_name = db.shorten_name(u'website_piece_concordance_imp')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_piece', models.ForeignKey(orm['website.piece'], null=False)),
            ('to_piece', models.ForeignKey(orm['website.piece'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_piece_id', 'to_piece_id'])

        # Adding M2M table for field genre_musical_normalise on 'Piece'
        m2m_table_name = db.shorten_name(u'website_piece_genre_musical_normalise')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('piece', models.ForeignKey(orm['website.piece'], null=False)),
            ('genremusicalnormalise', models.ForeignKey(orm['website.genremusicalnormalise'], null=False))
        ))
        db.create_unique(m2m_table_name, ['piece_id', 'genremusicalnormalise_id'])

        # Adding M2M table for field genre_musical_detaille on 'Piece'
        m2m_table_name = db.shorten_name(u'website_piece_genre_musical_detaille')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('piece', models.ForeignKey(orm['website.piece'], null=False)),
            ('genremusicaldetaille', models.ForeignKey(orm['website.genremusicaldetaille'], null=False))
        ))
        db.create_unique(m2m_table_name, ['piece_id', 'genremusicaldetaille_id'])

        # Adding model 'Recueil'
        db.create_table(u'website_recueil', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titre', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('titre_traduit', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('support', self.gf('django.db.models.fields.CharField')(default='imp', max_length=3)),
            ('ville_edition', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='lieu_d_edition_de', null=True, to=orm['website.Localisation'])),
            ('datation', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('editeur', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='editions', null=True, to=orm['website.Personne'])),
            ('compositeurs', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Personne'], null=True, blank=True)),
            ('nombre_pieces', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True, blank=True)),
            ('cahiers', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True, blank=True)),
            ('cahiers_manquants', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True, blank=True)),
            ('remarques', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('website', ['Recueil'])

        # Adding M2M table for field catalogue_id on 'Recueil'
        m2m_table_name = db.shorten_name(u'website_recueil_catalogue_id')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recueil', models.ForeignKey(orm['website.recueil'], null=False)),
            ('catalogue', models.ForeignKey(orm['website.catalogue'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recueil_id', 'catalogue_id'])

        # Adding M2M table for field genre_musical_normalise on 'Recueil'
        m2m_table_name = db.shorten_name(u'website_recueil_genre_musical_normalise')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recueil', models.ForeignKey(orm['website.recueil'], null=False)),
            ('genremusicalnormalise', models.ForeignKey(orm['website.genremusicalnormalise'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recueil_id', 'genremusicalnormalise_id'])

        # Adding M2M table for field genre_musical_detaille on 'Recueil'
        m2m_table_name = db.shorten_name(u'website_recueil_genre_musical_detaille')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recueil', models.ForeignKey(orm['website.recueil'], null=False)),
            ('genremusicaldetaille', models.ForeignKey(orm['website.genremusicaldetaille'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recueil_id', 'genremusicaldetaille_id'])

        # Adding M2M table for field reemission on 'Recueil'
        m2m_table_name = db.shorten_name(u'website_recueil_reemission')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_recueil', models.ForeignKey(orm['website.recueil'], null=False)),
            ('to_recueil', models.ForeignKey(orm['website.recueil'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_recueil_id', 'to_recueil_id'])

        # Adding M2M table for field reedition on 'Recueil'
        m2m_table_name = db.shorten_name(u'website_recueil_reedition')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_recueil', models.ForeignKey(orm['website.recueil'], null=False)),
            ('to_recueil', models.ForeignKey(orm['website.recueil'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_recueil_id', 'to_recueil_id'])

        # Adding M2M table for field projet on 'Recueil'
        m2m_table_name = db.shorten_name(u'website_recueil_projet')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recueil', models.ForeignKey(orm['website.recueil'], null=False)),
            ('projet', models.ForeignKey(orm['website.projet'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recueil_id', 'projet_id'])

        # Adding model 'Projet'
        db.create_table(u'website_projet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom_du_projet', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('liens_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('website', ['Projet'])

        # Adding model 'GenreMusicalNormalise'
        db.create_table(u'website_genremusicalnormalise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('style', self.gf('django.db.models.fields.CharField')(default='profane', max_length=128)),
            ('provenance', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('website', ['GenreMusicalNormalise'])

        # Adding model 'Categorie'
        db.create_table(u'website_categorie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('website', ['Categorie'])

        # Adding model 'Article'
        db.create_table(u'website_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('auteur', self.gf('django.db.models.fields.related.ForeignKey')(related_name='actualites', to=orm['auth.User'])),
            ('contenu', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('lien', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('categorie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Categorie'])),
        ))
        db.send_create_signal('website', ['Article'])

        # Adding model 'Voix'
        db.create_table(u'website_voix', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('voix', self.gf('django.db.models.fields.CharField')(default='Cantus', max_length=128)),
        ))
        db.send_create_signal('website', ['Voix'])

        # Adding model 'Exemplaire'
        db.create_table(u'website_exemplaire', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('localisation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Bibliotheque'], null=True, blank=True)),
            ('cote_exemplaire', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('etat', self.gf('django.db.models.fields.CharField')(default='CO', max_length=3)),
            ('remarques', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('lien_source', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('website', ['Exemplaire'])

        # Adding M2M table for field voix on 'Exemplaire'
        m2m_table_name = db.shorten_name(u'website_exemplaire_voix')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('exemplaire', models.ForeignKey(orm['website.exemplaire'], null=False)),
            ('voix', models.ForeignKey(orm['website.voix'], null=False))
        ))
        db.create_unique(m2m_table_name, ['exemplaire_id', 'voix_id'])


    def backwards(self, orm):
        # Deleting model 'Localisation'
        db.delete_table(u'website_localisation')

        # Deleting model 'Bibliotheque'
        db.delete_table(u'website_bibliotheque')

        # Deleting model 'Role'
        db.delete_table(u'website_role')

        # Deleting model 'Personne'
        db.delete_table(u'website_personne')

        # Removing M2M table for field role on 'Personne'
        db.delete_table(db.shorten_name(u'website_personne_role'))

        # Removing M2M table for field lieu_activite on 'Personne'
        db.delete_table(db.shorten_name(u'website_personne_lieu_activite'))

        # Deleting model 'GenreMusicalDetaille'
        db.delete_table(u'website_genremusicaldetaille')

        # Deleting model 'Catalogue'
        db.delete_table(u'website_catalogue')

        # Deleting model 'Piece'
        db.delete_table(u'website_piece')

        # Removing M2M table for field concordance_ms on 'Piece'
        db.delete_table(db.shorten_name(u'website_piece_concordance_ms'))

        # Removing M2M table for field concordance_imp on 'Piece'
        db.delete_table(db.shorten_name(u'website_piece_concordance_imp'))

        # Removing M2M table for field genre_musical_normalise on 'Piece'
        db.delete_table(db.shorten_name(u'website_piece_genre_musical_normalise'))

        # Removing M2M table for field genre_musical_detaille on 'Piece'
        db.delete_table(db.shorten_name(u'website_piece_genre_musical_detaille'))

        # Deleting model 'Recueil'
        db.delete_table(u'website_recueil')

        # Removing M2M table for field catalogue_id on 'Recueil'
        db.delete_table(db.shorten_name(u'website_recueil_catalogue_id'))

        # Removing M2M table for field genre_musical_normalise on 'Recueil'
        db.delete_table(db.shorten_name(u'website_recueil_genre_musical_normalise'))

        # Removing M2M table for field genre_musical_detaille on 'Recueil'
        db.delete_table(db.shorten_name(u'website_recueil_genre_musical_detaille'))

        # Removing M2M table for field reemission on 'Recueil'
        db.delete_table(db.shorten_name(u'website_recueil_reemission'))

        # Removing M2M table for field reedition on 'Recueil'
        db.delete_table(db.shorten_name(u'website_recueil_reedition'))

        # Removing M2M table for field projet on 'Recueil'
        db.delete_table(db.shorten_name(u'website_recueil_projet'))

        # Deleting model 'Projet'
        db.delete_table(u'website_projet')

        # Deleting model 'GenreMusicalNormalise'
        db.delete_table(u'website_genremusicalnormalise')

        # Deleting model 'Categorie'
        db.delete_table(u'website_categorie')

        # Deleting model 'Article'
        db.delete_table(u'website_article')

        # Deleting model 'Voix'
        db.delete_table(u'website_voix')

        # Deleting model 'Exemplaire'
        db.delete_table(u'website_exemplaire')

        # Removing M2M table for field voix on 'Exemplaire'
        db.delete_table(db.shorten_name(u'website_exemplaire_voix'))


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
            'choix_catalogue': ('django.db.models.fields.CharField', [], {'default': "'RA'", 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifiant': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'})
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
            'genre_musical': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255'}),
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
            'formation': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'genre_musical_detaille': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'pieces'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['website.GenreMusicalDetaille']"}),
            'genre_musical_normalise': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'pieces'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['website.GenreMusicalNormalise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mei_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'nombre_de_voix': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'nombre_de_voix_manquante': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'pdf_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'poete': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Personne']", 'null': 'True', 'blank': 'True'}),
            'recueil_id': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'pieces'", 'null': 'True', 'to': "orm['website.Recueil']"}),
            'remarques': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'website.projet': {
            'Meta': {'object_name': 'Projet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'liens_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'nom_du_projet': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'website.recueil': {
            'Meta': {'object_name': 'Recueil'},
            'cahiers': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'cahiers_manquants': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'catalogue_id': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'recueil'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['website.Catalogue']"}),
            'compositeurs': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Personne']", 'null': 'True', 'blank': 'True'}),
            'datation': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'editeur': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'editions'", 'null': 'True', 'to': "orm['website.Personne']"}),
            'genre_musical_detaille': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'recueils'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['website.GenreMusicalDetaille']"}),
            'genre_musical_normalise': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'recueils'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['website.GenreMusicalNormalise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_pieces': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'projet': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'dans'", 'symmetrical': 'False', 'to': "orm['website.Projet']"}),
            'reedition': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'reedition_rel_+'", 'null': 'True', 'to': "orm['website.Recueil']"}),
            'reemission': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'reemission_rel_+'", 'null': 'True', 'to': "orm['website.Recueil']"}),
            'remarques': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'support': ('django.db.models.fields.CharField', [], {'default': "'imp'", 'max_length': '3'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'titre_traduit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ville_edition': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'lieu_d_edition_de'", 'null': 'True', 'to': "orm['website.Localisation']"})
        },
        'website.role': {
            'Meta': {'object_name': 'Role'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'website.voix': {
            'Meta': {'object_name': 'Voix'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'voix': ('django.db.models.fields.CharField', [], {'default': "'Cantus'", 'max_length': '128'})
        }
    }

    complete_apps = ['website']