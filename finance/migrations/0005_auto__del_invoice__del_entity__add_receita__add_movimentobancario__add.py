# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Invoice'
        db.delete_table(u'finance_invoice')

        # Deleting model 'Entity'
        db.delete_table(u'finance_entity')

        # Adding model 'Receita'
        db.create_table(u'finance_receita', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entidade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finance.Entidade'])),
            ('valor', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal(u'finance', ['Receita'])

        # Adding model 'MovimentoBancario'
        db.create_table(u'finance_movimentobancario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('conta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finance.ContaBancaria'])),
            ('data_valor', self.gf('django.db.models.fields.DateField')()),
            ('data_movimento', self.gf('django.db.models.fields.DateField')()),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('montante', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal(u'finance', ['MovimentoBancario'])

        # Adding model 'Entidade'
        db.create_table(u'finance_entidade', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nif', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('morada', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'finance', ['Entidade'])

        # Adding model 'Despesa'
        db.create_table(u'finance_despesa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data', self.gf('django.db.models.fields.DateField')()),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pago', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'finance', ['Despesa'])

        # Adding model 'LinhaFatura'
        db.create_table(u'finance_linhafatura', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fatura', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finance.Fatura'])),
            ('iva', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('valor', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal(u'finance', ['LinhaFatura'])

        # Adding model 'ContaBancaria'
        db.create_table(u'finance_contabancaria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'finance', ['ContaBancaria'])

        # Adding model 'Fatura'
        db.create_table(u'finance_fatura', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entidade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finance.Entidade'])),
            ('data', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'finance', ['Fatura'])


    def backwards(self, orm):
        # Adding model 'Invoice'
        db.create_table(u'finance_invoice', (
            ('value', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finance.Entity'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('z', self.gf('django.db.models.fields.CharField')(default='ok', max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'finance', ['Invoice'])

        # Adding model 'Entity'
        db.create_table(u'finance_entity', (
            ('vat', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'finance', ['Entity'])

        # Deleting model 'Receita'
        db.delete_table(u'finance_receita')

        # Deleting model 'MovimentoBancario'
        db.delete_table(u'finance_movimentobancario')

        # Deleting model 'Entidade'
        db.delete_table(u'finance_entidade')

        # Deleting model 'Despesa'
        db.delete_table(u'finance_despesa')

        # Deleting model 'LinhaFatura'
        db.delete_table(u'finance_linhafatura')

        # Deleting model 'ContaBancaria'
        db.delete_table(u'finance_contabancaria')

        # Deleting model 'Fatura'
        db.delete_table(u'finance_fatura')


    models = {
        u'finance.contabancaria': {
            'Meta': {'object_name': 'ContaBancaria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'finance.despesa': {
            'Meta': {'object_name': 'Despesa'},
            'data': ('django.db.models.fields.DateField', [], {}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pago': ('django.db.models.fields.BooleanField', [], {})
        },
        u'finance.entidade': {
            'Meta': {'object_name': 'Entidade'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'morada': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nif': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'finance.fatura': {
            'Meta': {'object_name': 'Fatura'},
            'data': ('django.db.models.fields.DateField', [], {}),
            'entidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finance.Entidade']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'finance.linhafatura': {
            'Meta': {'object_name': 'LinhaFatura'},
            'fatura': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finance.Fatura']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iva': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'valor': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'finance.movimentobancario': {
            'Meta': {'object_name': 'MovimentoBancario'},
            'conta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finance.ContaBancaria']"}),
            'data_movimento': ('django.db.models.fields.DateField', [], {}),
            'data_valor': ('django.db.models.fields.DateField', [], {}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'montante': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'finance.receita': {
            'Meta': {'object_name': 'Receita'},
            'entidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finance.Entidade']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'valor': ('django.db.models.fields.FloatField', [], {'default': '0'})
        }
    }

    complete_apps = ['finance']