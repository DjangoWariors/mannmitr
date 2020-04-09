from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars

# Create your models here.
class SidebarImage(models.Model):
    #title = models.CharField(max_length=50,null=True)
    image = models.ImageField(upload_to='sidebar/%Y/%m/%d')
    creation_date = models.DateTimeField(auto_now_add=True,editable=False)
    last_update = models.DateTimeField(auto_now=True)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

class SidebarTitle(models.Model):
    title = models.CharField(max_length=50,null=True)
    creation_date = models.DateTimeField(auto_now_add=True,editable=False)
    last_update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title