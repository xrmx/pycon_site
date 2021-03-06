# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SlideControl'
        db.create_table(u'cms_utils_slidecontrol', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('fade', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('automatic', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('timeout', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=3000)),
            ('arrows', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('border', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'cms_utils', ['SlideControl'])


    def backwards(self, orm):
        # Deleting model 'SlideControl'
        db.delete_table(u'cms_utils_slidecontrol')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'cms_utils.markituppluginmodel': {
            'Meta': {'object_name': 'MarkitUpPluginModel', '_ormbases': ['cms.CMSPlugin']},
            u'_body_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'body': ('markitup.fields.MarkupField', [], {u'no_rendered_field': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'cms_utils.slidecontrol': {
            'Meta': {'object_name': 'SlideControl', '_ormbases': ['cms.CMSPlugin']},
            'arrows': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'automatic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'border': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'fade': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'timeout': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '3000'})
        }
    }

    complete_apps = ['cms_utils']