# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Invoice.z'
        db.add_column(u'finance_invoice', 'z',
                      self.gf('django.db.models.fields.CharField')(default='ok', max_length=100),
                      keep_default=False)


        # Changing field 'Invoice.date'
        db.alter_column(u'finance_invoice', 'date', self.gf('django.db.models.fields.DateField')())

    def backwards(self, orm):
        # Deleting field 'Invoice.z'
        db.delete_column(u'finance_invoice', 'z')


        # Changing field 'Invoice.date'
        db.alter_column(u'finance_invoice', 'date', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        u'finance.entity': {
            'Meta': {'object_name': 'Entity'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'vat': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'finance.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finance.Entity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'z': ('django.db.models.fields.CharField', [], {'default': "'ok'", 'max_length': '100'})
        }
    }

    complete_apps = ['finance']