# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.file
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__latest__'),
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='ButtonPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('url', models.URLField(null=True, verbose_name='Link', blank=True)),
                ('anchor', models.CharField(help_text='An anchor has priority over a text link.', max_length=100, null=True, verbose_name='Anchor', blank=True)),
                ('mailto', models.EmailField(help_text='An email adress has priority over a page link.', max_length=254, null=True, verbose_name='Mailto', blank=True)),
                ('phone', models.CharField(help_text='A phone number has priority over a mailto link.', max_length=40, null=True, verbose_name='Phone', blank=True)),
                ('target', models.CharField(blank=True, max_length=100, verbose_name='target', choices=[(b'', 'same window'), (b'_blank', 'new window'), (b'_parent', 'parent window'), (b'_top', 'topmost frame')])),
                ('css_classes', models.CharField(max_length=255, null=True, verbose_name='css classes', blank=True)),
                ('css_id', models.CharField(max_length=255, null=True, verbose_name='css id', blank=True)),
                ('file', filer.fields.file.FilerFileField(blank=True, to='filer.File', help_text='A file has priority over a phone number.', null=True, verbose_name='File')),
                ('page_link', cms.models.fields.PageField(blank=True, to='cms.Page', help_text='A link to a page has priority over an anchor.', null=True, verbose_name='Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
