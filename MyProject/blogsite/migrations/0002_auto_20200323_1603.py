# Generated by Django 3.0 on 2020-03-23 10:33

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expert',
            name='contact_info',
            field=djrichtextfield.models.RichTextField(),
        ),
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=djrichtextfield.models.RichTextField(),
        ),
    ]
