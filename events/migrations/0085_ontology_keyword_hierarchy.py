# Generated by Django 2.2.24 on 2022-01-18 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0084_keyword_is_hidden'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyword',
            name='children',
            field=models.ManyToManyField(blank=True, related_name='_keyword_children_+', to='events.Keyword'),
        ),
        migrations.AddField(
            model_name='keyword',
            name='ontology_type',
            field=models.SmallIntegerField(
                choices=[(1, 'OntologyConcept'), (2, 'OntologyHierarchy')], default=1, verbose_name='Ontology type'),
        ),
        migrations.AddField(
            model_name='keyword',
            name='parents',
            field=models.ManyToManyField(blank=True, related_name='_keyword_parents_+', to='events.Keyword'),
        ),
    ]
