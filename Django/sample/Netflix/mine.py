from django.urls import path, include
from . import views

urlpatterns =[
    path('',views.first),
    path('room/',views.room),
    path('nav/<str:m>/',views.nav),
    path('mine/',views.mine)
]