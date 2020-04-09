from django.db import models
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars
# Create your models here.
class AboutFounder(models.Model):

    ENGLISH = 'EN'
    HINDI = 'IN'
    LANGUAGE_TYPE = (
        (ENGLISH, 'English'),
        (HINDI, 'Hindi'),
    )

    name = models.CharField(max_length=30)
    language = models.CharField(max_length=10, choices = LANGUAGE_TYPE,null=True)
    content = RichTextField()
    image = models.ImageField(upload_to='photos/aboutFounders',null=True)
    creation_date = models.DateTimeField(auto_now_add=True,editable=False)
    last_update = models.DateTimeField(auto_now=True)

    @property
    def short_description(self):
        return truncatechars(self.content, 50)
    def aboutus_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))
    aboutus_photo.short_description = 'Image'
    aboutus_photo.allow_tags = True

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "About Founder"
        verbose_name_plural = "About Founder"
class AboutUs(models.Model):
    ENGLISH = 'EN'
    HINDI = 'IN'
    LANGUAGE_TYPE = (
        (ENGLISH, 'English'),
        (HINDI, 'Hindi'),
    )
    language = models.CharField(max_length=10, choices = LANGUAGE_TYPE,null=True)
    content = RichTextField()
    creation_date = models.DateTimeField(auto_now_add=True,editable=False)
    last_update = models.DateTimeField(auto_now=True)
    @property
    def short_description(self):
        return truncatechars(self.content, 50)

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"
