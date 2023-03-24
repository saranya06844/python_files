from django.urls import path
from details import views

urlpatterns =[
    path('home',views.Student_entryList.as_view(),name='home'),
    path('studentdetail/<int:pk>',views.Student_entryDetail.as_view(),name='studentdetail'),
    path('studentcreate',views.Student_entryCreate.as_view(),name='studentcreate'),
    path('studentdelete/<int:pk>',views.Student_entryDelete.as_view(),name='studentdelete'),
    path('studentupdate/<int:pk>',views.Student_entryUpdate.as_view(),name='studentupdate'),
    
    
]