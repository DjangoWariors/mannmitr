# Generated by Django 3.0 on 2020-04-06 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hindiblogsite', '0004_hindiposts_youtubelink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hindiposts',
            name='language',
        ),
        migrations.AddField(
            model_name='hindiposts',
            name='slider',
            field=models.CharField(choices=[('T', 'True'), ('F', 'False')], max_length=10, null=True),
        ),
    ]