# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Household'
        db.create_table(u'paris_household', (
            ('household_name', self.gf('django.db.models.fields.CharField')(max_length=120, primary_key=True)),
        ))
        db.send_create_signal(u'paris', ['Household'])

        # Adding model 'User'
        db.create_table(u'paris_user', (
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('household_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['paris.Household'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'paris', ['User'])

        # Adding model 'Wallet'
        db.create_table(u'paris_wallet', (
            ('user_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['paris.User'], primary_key=True)),
            ('balance', self.gf('django.db.models.fields.DecimalField')(max_digits=50, decimal_places=2)),
            ('household_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['paris.Household'])),
        ))
        db.send_create_signal(u'paris', ['Wallet'])


    def backwards(self, orm):
        # Deleting model 'Household'
        db.delete_table(u'paris_household')

        # Deleting model 'User'
        db.delete_table(u'paris_user')

        # Deleting model 'Wallet'
        db.delete_table(u'paris_wallet')


    models = {
        u'paris.household': {
            'Meta': {'object_name': 'Household'},
            'household_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'primary_key': 'True'})
        },
        u'paris.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'household_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['paris.Household']"}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'})
        },
        u'paris.wallet': {
            'Meta': {'object_name': 'Wallet'},
            'balance': ('django.db.models.fields.DecimalField', [], {'max_digits': '50', 'decimal_places': '2'}),
            'household_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['paris.Household']"}),
            'user_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['paris.User']", 'primary_key': 'True'})
        }
    }

    complete_apps = ['paris']