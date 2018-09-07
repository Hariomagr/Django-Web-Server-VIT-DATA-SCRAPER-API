from django.urls import path
from . import views
urlpatterns = [
    path('timetable/', views.home,name='api-home'),
    path('attendance/', views.attandence,name='api-attandence'),
    path('assignment/', views.assignment,name='api-assignment'),
    path('curriculum/', views.curriculum,name='api-curriculum'),
    path('exam/', views.exam,name='api-exam'),
    path('marks/', views.marks,name='api-marks'),
    path('grade_history/', views.grade_history,name='api-grade_history'),
    path('grade_semwise/', views.grade_semwise,name='api-grade_semwise'),
]
