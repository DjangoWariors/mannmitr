
from django.contrib import admin
from django.db import models
from . models import contact,internship
import csv
from django.http import HttpResponse

admin.site.site_header = " Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Admin"
# Register your models here.
# Register your models here.
class contactAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    def download_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response
        
    download_csv.short_description = "Export Selected"
    
    list_display = [
        'Name',
        'phone',
        'email',
        'message',
        'creation_date'
    ]
    
    list_filter = [
         
        'creation_date'
    ]
    date_hierarchy = 'creation_date'
admin.site.register(contact,contactAdmin)

class internshipAdmin(admin.ModelAdmin):
    #fields = ("Name", 'phone','email','message','CV')
    actions = ['download_csv']
    def download_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response
        
    download_csv.short_description = "Export Selected"
    list_display = [
        'Name',
        'phone',
        'email',
        'message',
        'CV',
        #'creation_date',
    ]
    list_filter = [
         
        'creation_date'
    ]
    date_hierarchy = 'creation_date'
admin.site.register(internship,internshipAdmin)