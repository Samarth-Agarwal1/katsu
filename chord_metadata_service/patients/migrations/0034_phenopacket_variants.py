# Generated by Django 2.2.6 on 2019-10-16 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0033_remove_phenopacket_variants'),
    ]

    operations = [
        migrations.AddField(
            model_name='phenopacket',
            name='variants',
            field=models.ManyToManyField(blank=True, to='patients.Variant'),
        ),
    ]
