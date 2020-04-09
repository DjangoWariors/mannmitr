from django.contrib import admin
from . models import SidebarImage,SidebarTitle
# Register your models here
class SidebarAdmin(admin.ModelAdmin):
    fields = ('image',)
    inline_type = 'tabular'
    list_display = [
        'admin_photo',
        'image',
        'creation_date'
    ]
    list_display_links=[
        'image',
    ]
    list_filter = [ 
        'creation_date'
    ]
    date_hierarchy = 'creation_date'
    readonly_fields = ('creation_date',)
admin.site.register(SidebarImage,SidebarAdmin)

class SidebarTitleAdmin(admin.ModelAdmin):
    fields = ('title',)
    inline_type = 'tabular'
    list_display = [
        'title',
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
    
admin.site.register(SidebarTitle,SidebarTitleAdmin)


