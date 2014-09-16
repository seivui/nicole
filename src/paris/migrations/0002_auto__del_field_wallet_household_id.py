# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Wallet.household_id'
        db.delete_column(u'paris_wallet', 'household_id_id')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Wallet.household_id'
        raise RuntimeError("Cannot reverse this migration. 'Wallet.household_id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Wallet.household_id'
        db.add_column(u'paris_wallet', 'household_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['paris.Household']),
                      keep_default=False)


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
            'user_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['paris.User']", 'primary_key': 'True'})
        }
    }

    complete_apps = ['paris']