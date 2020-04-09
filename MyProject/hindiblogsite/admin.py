from django.contrib import admin
from django.db import models
from . models import HindiCategory,HindiSubcategory,HindiPosts

from django.contrib.auth.models import User, Group 
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

admin.site.site_header = " Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Admin"
# Register your models here.

class appAdmin(admin.ModelAdmin):
    #actions_selection_counter = False
    #actions_on_bottom = False
    #actions_on_top = True
    
    fields = (("expert",'status','slider'), ('category','Subcategory'),'title','content', 'image', 'admin_photo')
    inline_type = 'tabular'
    list_display = [
        'admin_photo',
        'expert',
        'title',
        'category',
        'Subcategory',
        'short_description',
        'status',
        
    ]
    list_display_links=[
        
        'title'
    ]
    list_filter = [
         
        'title',
        'creation_date'
    ]
    date_hierarchy = 'creation_date'
    
    readonly_fields = ('creation_date','admin_photo')
    
admin.site.register(HindiPosts,appAdmin)

class CategoryAdmin(admin.ModelAdmin):
    fields = ('category',)
    inline_type = 'tabular'
    list_display = [
        'category',
    ]
    list_display_links=[
        'category'
    ]
    list_filter =['category']
    #search_fields = ['category','Sub_Tabs']

admin.site.register(HindiCategory,CategoryAdmin)



class SubcategoryAdmin(admin.ModelAdmin):
    fields = ('category','sub_category')
    inline_type = 'tabular'
    list_display = [
        'category',
        'sub_category',
        
        
    ]
    list_display_links=[
        'sub_category'
    ]
    list_filter =['category']
    #search_fields = ['category','Sub_Tabs']

admin.site.register(HindiSubcategory,SubcategoryAdmin)
"""
class SubcategoryInline(admin.TabularInline):
    model = Subcategory

class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SubcategoryInline,
    ]

admin.site.register(Category,CategoryAdmin)
"""
