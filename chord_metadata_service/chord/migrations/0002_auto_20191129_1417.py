# Generated by Django 2.2.7 on 2019-11-29 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chord', '0001_initial'),
        ('phenopackets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tableownership',
            name='sample',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='phenopackets.Biosample'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='has_part',
            field=models.ManyToManyField(blank=True, help_text="A Dataset that is a subset of this Dataset; Datasets declaring the 'hasPart' relationship are considered a collection of Datasets, the aggregation criteria could be included in the 'description' field.", related_name='_dataset_has_part_+', to='chord.Dataset'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datasets', to='chord.Project'),
        ),
    ]