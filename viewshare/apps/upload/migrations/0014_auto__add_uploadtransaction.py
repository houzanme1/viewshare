# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UploadTransaction'
        db.create_table(u'upload_uploadtransaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('is_complete', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('result', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tx_id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='transactions', to=orm['upload.DataSource'])),
        ))
        db.send_create_signal(u'upload', ['UploadTransaction'])


    def backwards(self, orm):
        # Deleting model 'UploadTransaction'
        db.delete_table(u'upload_uploadtransaction')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'exhibit.canvas': {
            'Meta': {'object_name': 'Canvas'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'title'", 'overwrite': 'False'}),
            'thumbnail': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'exhibit.exhibit': {
            'Meta': {'unique_together': "(('owner', 'slug', 'is_draft'),)", 'object_name': 'Exhibit'},
            'canvas': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exhibit.Canvas']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'profile': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'exhibit.publishedexhibit': {
            'Meta': {'ordering': "('-modified',)", 'object_name': 'PublishedExhibit', '_ormbases': [u'exhibit.Exhibit']},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'exhibit_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['exhibit.Exhibit']", 'unique': 'True', 'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'upload.contentdmdatasource': {
            'Meta': {'object_name': 'ContentDMDataSource', '_ormbases': [u'upload.DataSource']},
            'collection': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'datasource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['upload.DataSource']", 'unique': 'True', 'primary_key': 'True'}),
            'limit': ('django.db.models.fields.IntegerField', [], {'default': "'100'"}),
            'query': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'upload.datasource': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'DataSource'},
            'classname': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'exhibit': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'source'", 'unique': 'True', 'to': u"orm['exhibit.Exhibit']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        u'upload.filedatasource': {
            'Meta': {'object_name': 'FileDataSource', '_ormbases': [u'upload.DataSource']},
            u'datasource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['upload.DataSource']", 'unique': 'True', 'primary_key': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255'})
        },
        u'upload.jsonfiledatasource': {
            'Meta': {'object_name': 'JSONFileDataSource', '_ormbases': [u'upload.DataSource']},
            u'datasource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['upload.DataSource']", 'unique': 'True', 'primary_key': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            'mapping': ('django.db.models.fields.TextField', [], {}),
            'path': ('django.db.models.fields.TextField', [], {})
        },
        u'upload.jsonurldatasource': {
            'Meta': {'object_name': 'JSONURLDataSource', '_ormbases': [u'upload.DataSource']},
            u'datasource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['upload.DataSource']", 'unique': 'True', 'primary_key': 'True'}),
            'mapping': ('django.db.models.fields.TextField', [], {}),
            'path': ('django.db.models.fields.TextField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'upload.modsfiledatasource': {
            'Meta': {'object_name': 'ModsFileDataSource', '_ormbases': [u'upload.DataSource']},
            u'datasource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['upload.DataSource']", 'unique': 'True', 'primary_key': 'True'}),
            'diagnostics': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255'})
        },
        u'upload.modsurldatasource': {
            'Meta': {'object_name': 'ModsURLDataSource', '_ormbases': [u'upload.DataSource']},
            u'datasource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['upload.DataSource']", 'unique': 'True', 'primary_key': 'True'}),
            'diagnostics': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'upload.oaidatasource': {
            'Meta': {'object_name': 'OAIDataSource', '_ormbases': [u'upload.DataSource']},
            u'datasource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['upload.DataSource']", 'unique': 'True', 'primary_key': 'True'}),
            'limit': ('django.db.models.fields.IntegerField', [], {'default': "'100'"}),
            'set': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'upload.referencedatasource': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'ReferenceDataSource', '_ormbases': [u'upload.DataSource']},
            u'datasource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['upload.DataSource']", 'unique': 'True', 'primary_key': 'True'}),
            'referenced': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'references'", 'to': u"orm['exhibit.PublishedExhibit']"})
        },
        u'upload.uploadtransaction': {
            'Meta': {'object_name': 'UploadTransaction'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'result': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'transactions'", 'to': u"orm['upload.DataSource']"}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'tx_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        u'upload.urldatasource': {
            'Meta': {'object_name': 'URLDataSource', '_ormbases': [u'upload.DataSource']},
            u'datasource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['upload.DataSource']", 'unique': 'True', 'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['upload']