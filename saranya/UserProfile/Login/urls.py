from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home, name = "home"),
    path('register/',views.register_request, name = "register"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('display/',views.display, name="display"),
    path('example/',views.example, name= "example"),
    path('add/',views.add, name='add')
]