from django.db import models
# Create your models here.
class Subscribe(models.Model):
    email = models.EmailField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True,editable=False,null=True)
    def __str__(self):
        return self.email

class Sendemail(models.Model):
    recipient = models.EmailField(max_length=200)
    subject = models.CharField(max_length=500)
    message = models.CharField(max_length=800)
    creation_date = models.DateTimeField(auto_now_add=True,editable=False,null=True)
    
    def __str__(self):
        return self.recipient
    
    class Meta:
        verbose_name = "Send Email"
        verbose_name_plural = "Send Email"

