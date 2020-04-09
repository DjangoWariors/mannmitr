# Generated by Django 3.0 on 2020-04-01 08:55

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(db_index=True, max_length=200)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_update', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'Hindi Tabs',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('education', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('expertise', models.CharField(max_length=200, null=True)),
                ('experience', models.CharField(max_length=50, null=True)),
                ('contact_info', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', models.ImageField(null=True, upload_to='expert/%Y/%m/%d')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category', models.CharField(db_index=True, max_length=200)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_update', models.DateTimeField(auto_now=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hindiblogsite.Category')),
            ],
            options={
                'verbose_name': 'sub category',
                'verbose_name_plural': 'Hindi Sub Tabs',
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('D', 'Draft'), ('P', 'Published')], max_length=10)),
                ('language', models.CharField(choices=[('EN', 'English'), ('IN', 'Hindi')], max_length=10)),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', models.ImageField(null=True, upload_to='photos/%Y/%m/%d')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('Subcategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hindiblogsite.Subcategory')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hindiblogsite.Category')),
                ('expert', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hindiblogsite.Expert')),
            ],
            options={
                'verbose_name': 'Hindi Posts',
                'verbose_name_plural': 'Hindi Posts',
            },
        ),
    ]
