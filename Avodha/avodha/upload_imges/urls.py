from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('',views.home,name= "home")
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)