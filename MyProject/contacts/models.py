from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars 

class contact(models.Model):
    Name = models.CharField(max_length=50) 
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=1000)
    creation_date = models.DateTimeField(auto_now_add=True,editable=False,null=True)
    def __str__(self):
        return self.Name

class internship(models.Model):
    Name = models.CharField(max_length=50) 
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=1000)
    CV = models.FileField(upload_to='uploadsCV/%y/%m/%d',null=True,blank=True)
    creation_date = models.DateTimeField(auto_now_add=True,editable=False,null=True)
    def __str__(self):
        return self.Name
    
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

    def cv(self):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'user_{0}/{1}'.format(self.CV.url)