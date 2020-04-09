from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars 
from ckeditor.fields import RichTextField

class MediaCoverage(models.Model):
    publication= models.CharField(max_length=500)
    synopsis = RichTextField()
    image = models.ImageField(upload_to='mediacoverage/%Y/%m/%d',height_field=None, width_field=None, null=True)
    Date = models.DateField()
    creation_date = models.DateTimeField(auto_now_add=True,editable=False,null=True)
    last_update = models.DateTimeField(auto_now=True ,null=True)
    class Meta: 
        ordering=("-creation_date",)
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True
    @property
    def short_description(self):
        return truncatechars(self.synopsis, 50)
    def __str__(self):
        return self.publication

class YouTubeLink(models.Model):
    title = models.CharField(max_length=50) 
    YoutubeLink = models.URLField(max_length=256)
    image = models.ImageField(upload_to='thumbnail/%Y/%m/%d',height_field=None, width_field=None, null=True)
    creation_date = models.DateTimeField(auto_now_add=True,editable=False,null=True)
    last_update = models.DateTimeField(auto_now=True ,null=True)
    class Meta:    
        ordering=("-creation_date",)
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

    def __str__(self):
        return self.title

