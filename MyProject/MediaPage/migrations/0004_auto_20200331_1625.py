# Generated by Django 3.0 on 2020-03-31 10:55

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MediaPage', '0003_auto_20200330_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediacoverage',
            name='publication',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='mediacoverage',
            name='synopsis',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
