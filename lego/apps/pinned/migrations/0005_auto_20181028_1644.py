# Generated by Django 2.0.6 on 2018-10-28 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pinned', '0004_auto_20181024_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pinnedarticle',
            name='article',
        ),
        migrations.RemoveField(
            model_name='pinnedarticle',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='pinnedarticle',
            name='target_groups',
        ),
        migrations.RemoveField(
            model_name='pinnedarticle',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='pinnedevent',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='pinnedevent',
            name='event',
        ),
        migrations.RemoveField(
            model_name='pinnedevent',
            name='target_groups',
        ),
        migrations.RemoveField(
            model_name='pinnedevent',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='PinnedArticle',
        ),
        migrations.DeleteModel(
            name='PinnedEvent',
        ),
    ]
