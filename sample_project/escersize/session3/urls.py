from django.urls import path
from . import views

urlpatterns =[
    path('welcome/',views.welcome),
    # add a static file
    path('add_static/',views.add_static)
]