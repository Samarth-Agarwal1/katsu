# Generated by Django 2.2.6 on 2019-11-22 21:48

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0038_auto_20191122_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individual',
            name='address_postal_code',
        ),
        migrations.AddField(
            model_name='individual',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='individual',
            name='extra_properties',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Extra properties that are not supported by current schema', null=True),
        ),
        migrations.AddField(
            model_name='individual',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]