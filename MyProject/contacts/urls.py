from django.urls import path

from . import views
 
urlpatterns = [ 
    path('contact/' ,views.contacts, name="contacts"),
    path('internship/' ,views.internships, name="internship"),
   
]
