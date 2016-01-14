# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-13 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_keywordset'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='publication_status',
            field=models.SmallIntegerField(choices=[(1, 'public'), (2, 'draft')], default=1, verbose_name='Event data publication status'),
        ),
        migrations.AlterField(
            model_name='keywordset',
            name='usage',
            field=models.SmallIntegerField(choices=[(1, 'any'), (2, 'keyword'), (3, 'audience')], default=1, verbose_name='Intended keyword usage'),
        ),
    ]
