# Generated by Django 3.0 on 2020-03-31 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0006_auto_20200323_2104'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('pk',), 'verbose_name': 'category', 'verbose_name_plural': 'Tabs'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'sub category', 'verbose_name_plural': 'Sub Tabs'},
        ),
    ]
