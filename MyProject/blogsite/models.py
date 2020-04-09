from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars 
from ckeditor_uploader.fields import  RichTextUploadingField

from ckeditor.fields import RichTextField

from django.contrib.auth.models import User

class Category(models.Model):
    category= models.CharField(max_length=200,
                            db_index=True)
    creation_date = models.DateTimeField(auto_now_add=True,editable=False,null=True)
    last_update = models.DateTimeField(auto_now=True ,null=True)
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Tabs'
        
        ordering=("pk",)

    def __str__(self):
        return self.category
 
class Subcategory(models.Model):
    
    sub_category = models.CharField(max_length=200,
                            db_index=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True,editable=False,null=True)
    last_update = models.DateTimeField(auto_now=True ,null=True)
    class Meta:
        verbose_name = 'sub category'
        verbose_name_plural = 'Sub Tabs'
    def __str__(self):
        return self.sub_category

class Expert(models.Model):
    name = models.CharField(max_length=50,null=True)
    education = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=50,null=True)
    expertise = models.CharField(max_length=200,null=True)
    experience = models.CharField(max_length=50,null=True)
    contact_info = RichTextUploadingField() 
    image = models.ImageField(upload_to='expert/%Y/%m/%d',height_field=None, width_field=None, null=True)
    creation_date = models.DateTimeField(auto_now_add=True,editable=False)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

class Posts(models.Model):
    DRAFT = 'D'
    PUBLISHED = 'P'
    ENTRY_STATUS = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    )
   
    ENGLISH = 'EN'
    HINDI = 'IN'
    LANGUAGE_TYPE = (
        (ENGLISH, 'English'),
        (HINDI, 'Hindi'),
    )
    SLIDER_up = 'U'
    SLIDER_OF = 'F'
    SLIDER_lw = 'L'
    SLIDER_TYPE = ( 
        (SLIDER_up, 'Upper Slider'),
        (SLIDER_OF, 'False'),
        (SLIDER_lw, 'Lower Slider'),
    )
    expert = models.ForeignKey(Expert, on_delete=models.SET_NULL,null=True)
    status = models.CharField(max_length=10, choices = ENTRY_STATUS)
    slider = models.CharField(max_length=10, choices = SLIDER_TYPE,null=True)
    language = models.CharField(max_length=10, choices = LANGUAGE_TYPE,null=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    #slug = models.SlugField(max_length=200,db_index=True)
    Subcategory = models.ForeignKey(Subcategory,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    YoutubeLink = models.URLField(max_length=256,null=True,blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d',height_field=None, width_field=None, null=True)
    creation_date = models.DateTimeField(auto_now_add=True,editable=False)
    last_update = models.DateTimeField(auto_now=True)
    
    @property
    def short_description(self):
        return truncatechars(self.content, 50)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))
    admin_photo.short_description = 'Thumbnail image'
    admin_photo.allow_tags = True
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Posts"
        verbose_name_plural = "Posts"

