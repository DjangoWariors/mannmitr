# Generated by Django 3.0 on 2020-03-23 15:27

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0003_auto_20200323_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expert',
            name='contact_info',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='contents'),
        ),
    ]