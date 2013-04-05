# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Group'
        db.delete_table(u'worksheets_group')

        # Adding model 'StudentGroup'
        db.create_table(u'worksheets_studentgroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'worksheets', ['StudentGroup'])


        # Changing field 'StudentNotebook.group'
        db.alter_column(u'worksheets_studentnotebook', 'group_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['worksheets.StudentGroup']))

        # Changing field 'GroupNotebook.group'
        db.alter_column(u'worksheets_groupnotebook', 'group_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['worksheets.StudentGroup']))

        # Changing field 'GroupAssignment.group'
        db.alter_column(u'worksheets_groupassignment', 'group_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['worksheets.StudentGroup']))

    def backwards(self, orm):
        # Adding model 'Group'
        db.create_table(u'worksheets_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'worksheets', ['Group'])

        # Deleting model 'StudentGroup'
        db.delete_table(u'worksheets_studentgroup')


        # Changing field 'StudentNotebook.group'
        db.alter_column(u'worksheets_studentnotebook', 'group_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['worksheets.Group']))

        # Changing field 'GroupNotebook.group'
        db.alter_column(u'worksheets_groupnotebook', 'group_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['worksheets.Group']))

        # Changing field 'GroupAssignment.group'
        db.alter_column(u'worksheets_groupassignment', 'group_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['worksheets.Group']))

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
        u'worksheets.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'evernote_note_guid': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'group_assignment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['worksheets.GroupAssignment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['worksheets.Student']"})
        },
        u'worksheets.groupassignment': {
            'Meta': {'object_name': 'GroupAssignment'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['worksheets.StudentGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'worksheets.groupnotebook': {
            'Meta': {'object_name': 'GroupNotebook'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['worksheets.StudentGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'worksheets.student': {
            'Meta': {'object_name': 'Student'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'evernote_user_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['worksheets.StudentGroup']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'worksheets.studentgroup': {
            'Meta': {'object_name': 'StudentGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'worksheets.studentnotebook': {
            'Meta': {'object_name': 'StudentNotebook'},
            'evernote_guid': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['worksheets.StudentGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['worksheets.Student']"})
        },
        u'worksheets.subject': {
            'Meta': {'object_name': 'Subject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['worksheets']