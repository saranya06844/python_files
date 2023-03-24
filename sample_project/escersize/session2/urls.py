from django.urls import path
from . import views

urlpatterns = [
    path('Gm/',views.Good_Morning),
    path('Ga/',views.Good_Afternoon),
    path('Ge/',views.Good_Evenig),
    path('Gn/',views.Good_Night),
    # urls for print greeting based on current time
    path('Greetings/',views.Greetings)
]