
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf. urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogsite.urls')),
    path('about/', include('About_us.urls')),
    path('', include('hindiblogsite.urls')),
    path('media/', include('MediaPage.urls')),
    path('partner/', include('contacts.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    #path('djrichtextfield/', include('djrichtextfield.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
