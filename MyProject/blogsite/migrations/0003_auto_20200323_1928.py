# Generated by Django 3.0 on 2020-03-23 13:58

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0002_auto_20200323_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expert',
            name='contact_info',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
