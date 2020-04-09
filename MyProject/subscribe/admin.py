from django.contrib import admin
from MyProject.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from . models import Subscribe,Sendemail
# Register your models here.
admin.site.register(Subscribe)

class SendemailAdmin(admin.ModelAdmin):
    actions = ['sendemail']
    def sendemail(self, request, queryset):
        
        for obj in queryset:
            subject = obj.subject
            message = obj.message
            recepient = obj.recipient
            print(recepient)
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        
    sendemail.short_description = "Send Email"
    
    list_display = [
        'recipient',
        'subject',
        'message',
    ]
    
    list_filter = [
         
        'creation_date'
    ]
    date_hierarchy = 'creation_date'
admin.site.register(Sendemail,SendemailAdmin)