from django.urls import path
from student import views
from django.contrib.auth.views import LoginView

urlpatterns = [

path('field-choice', views.field_choice,name='field-choice'),
path('instruction/<int:pk>', views.instruction,name='instruction'),
path('start-exam/<int:pk>', views.start_exam_view,name='start-exam'),
path('set-timer/<int:pk>', views.set_timer,name='set-timer'),
path('suspicious', views.suspicious,name='suspicious'),

path('calculate-marks', views.calculate_marks_view,name='calculate-marks')
]