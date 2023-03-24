from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home),
    path('category/',views.category),
    path('contact/',views.contact),
    path('listing/',views.listing),
    path('image/',views.image)
]