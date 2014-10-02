# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Transaction'
        db.delete_table(u'finance_transaction')

        # Deleting model 'Provider'
        db.delete_table(u'finance_provider')

        # Adding model 'Invoice'
        db.create_table(u'finance_invoice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finance.Entity'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('value', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal(u'finance', ['Invoice'])


    def backwards(self, orm):
        # Adding model 'Transaction'
        db.create_table(u'finance_transaction', (
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'finance', ['Transaction'])

        # Adding model 'Provider'
        db.create_table(u'finance_provider', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'finance', ['Provider'])

        # Deleting model 'Invoice'
        db.delete_table(u'finance_invoice')


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
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finance.Entity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.FloatField', [], {'default': '0'})
        }
    }

    complete_apps = ['finance']