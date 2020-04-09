# Generated by Django 3.0 on 2020-04-06 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0010_posts_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='slider',
            field=models.CharField(choices=[('U', 'Upper Slider'), ('F', 'False'), ('L', 'Lower Slider')], max_length=10, null=True),
        ),
    ]