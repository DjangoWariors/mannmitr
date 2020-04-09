from django.contrib import admin
from django.db import models
from . models import MediaCoverage,YouTubeLink
from django.contrib.auth.models import User, Group 
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

admin.site.site_header = " Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Admin"
# Register your models here.

class MediaCoverageAdmin(admin.ModelAdmin):
   
    fields = (("publication",'Date'), 'synopsis','image')
    inline_type = 'tabular'
    list_display = [
        'admin_photo',
        'publication',
        'short_description',
        'Date',
    ]
    list_display_links=[
        
        'publication',
    ]
    list_filter = [ 
        'publication',
        'creation_date'
    ]
    date_hierarchy = 'creation_date'
    
    readonly_fields = ('creation_date',)
    
admin.site.register(MediaCoverage,MediaCoverageAdmin)

class YouTubeLinkAdmin(admin.ModelAdmin):
    fields = ("title", 'YoutubeLink',)
    inline_type = 'tabular'
    list_display = [
        
        'title',
        'YoutubeLink',
        'creation_date'
    ]
    list_display_links=[
        
        'title',
    ]
    list_filter = [
         
        'creation_date'
    ]
    date_hierarchy = 'creation_date'
    
    readonly_fields = ('creation_date',)
    
admin.site.register(YouTubeLink,YouTubeLinkAdmin)

