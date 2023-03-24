from django.urls import  path
from . import views

urlpatterns =[
    path('Students/',views.sample),
    path('StudentInfo/',views.StudentForm),
    path('cookie_count/',views.Cookies_count_view),
    path('session_count/',views.Session_count_view),
    path('dbstudent/',views.Student_info,name = 'display'),
    path('update/',views.Add_student,name = 'update'),
    path('delete/<id>/',views.delete_view,name = 'delete'),
    path('update/<id>/',views.update_view,name = 'updateid')

]

