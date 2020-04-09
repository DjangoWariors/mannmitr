from django.contrib import admin
from django.db import models
from . models import AboutUs,AboutFounder

class AboutFounderAdmin(admin.ModelAdmin):
    fields = (('name','language'),'content','image')
    inline_type = 'tabular'
    list_display = [
        'aboutus_photo',
        'name',
        'short_description',
        'creation_date',
    ]
    list_display_links=[
        'name',
    ]
    list_filter =['name']

admin.site.register(AboutFounder,AboutFounderAdmin)

class AboutUsAdmin(admin.ModelAdmin):
    fields = ('language','content',)
    inline_type = 'tabular'
    list_display = [
        'short_description',
        'creation_date',
    ]
    list_display_links=[
        'short_description',
    ]
    list_filter =['creation_date']

admin.site.register(AboutUs,AboutUsAdmin)
