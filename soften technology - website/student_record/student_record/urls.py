from django.contrib import admin  
from django.urls import path ,include

 
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('fileupload', include('fileupload.urls')),  
    path('',include('details.urls')),
    path('sections',include('sections.urls')),
]  